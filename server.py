
import numpy
import flask
import sqlite3

class JobPost:

    status = "open"
    module = "none"
    checked_out = False
    time_posted = ""
    time_completed = ""
    bpf = ""
    newrules = ""
    completedby = ""

    def read(self):
        return self.status,self.module,self.time_posted,self.time_completed,self.bpf,self.newrules,self.completedby


apikey = "TEST"
job1=JobPost

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except ConnectionError as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except ConnectionError as e:
        print(e)


def add_job():
    database = "nightwatch.db"

    sql_create_job_row"""INSERT INTO jobs(id, name, status, module, time_posted, time_completed, bpf, newrules, splunk, completedby)
    VALUES($idNum,$jobname,"working",$steno,$timeposted,"",$bpf,$snortrules,$splunk,"");
    """


def seed_db():
    database = "nightwatch.db"

    sql_create_jobs_table = """ CREATE TABLE IF NOT EXISTS jobs (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        status text,
                                        module text,
                                        time_posted text,
                                        time_completed text,
                                        bpf text,
                                        newrules text,
                                        splunk text,
                                        completedby text
                                    ); """
    # create a database connection
    conn = create_connection(database)
    conn = None
    conn = sqlite3.connect(database)
    # create tables
    if conn is not None:
        # create jobs table
        create_table(conn, sql_create_jobs_table)
        conn.close()

    else:
        print("Error! I cannot create the database connection.")


def job_board():  # Handles holding all the jobs for the watchmen to run##
    job_array = numpy.array(job1().read())

    board = flask.Flask(__name__)
    board.config["DEBUG"] = False

    @board.route('/', methods=['GET'])
    def home():
        text = "<p> Nightwatch is patrolling </p>"
        return text

    @board.route('/jobs', methods=['GET'])
    def jobs():
        if flask.request.headers['API-Key'] is not None:
            if flask.request.headers['API-Key'] == apikey:
                return str(job_array)
            else:
                return "Not Authenticated"
        else:
            return "Did you forget your keys at home?"
    while True:
        board.run()



job_board()
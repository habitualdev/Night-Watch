# #Modular python server/client framework for Night Owl##
# #IMPORTS
import requests
import json
import sys
import subprocess
import numpy
import flask
# #Classes

json_template={
  "job": {
    "id": {},
    "created": {},
    "completedby": {},
    "all_done": {}
  },
  "module": {
    "steno": {
      "bpf": {}
    },
    "pulledpork": {
      "newrules": {}
    }
  }
}


class JobPost:
    status = "open"
    module = "none"
    checked_out = False
    time_posted = ""
    time_completed = ""
    bpf = ""
    newrules = ""
    completedby = ""

# ##Command and control functions###

apikey = "TEST"

def get_job():
    # Exists to query the job board for stuff to do
    job= ""
    return job


def run_job():  # Queueing service to run jobs
    return()


def push_results():  # Returns job results to the job board
    return()


def job_board():  # Handles holding all the jobs for the watchmen to run##

    job_array = numpy.array('{"id": 1,"first_name": "Jeanette","last_name": "Penddreth","email": "jpenddreth0@census.gov","gender": "Female","ip_address": "26.58.193.2"}}')

    board = flask.Flask(__name__)
    board.config["DEBUG"] = True

    @board.route('/', methods=['GET'])
    def home():
        text = "<p> Nightwatch is patrolling </p>"
        return text

    @board.route('/jobs', methods=['GET'])
    def jobs():
        if flask.request.headers['API-Key'] == apikey:
            for jjob in job_array:


            return str(job_array)
        else:
            return "Not Authenticated"
    board.run()


def get_role():  # Tells if host is a job board or watchman
    filename = "watch.json"
    with open(filename, "ro") as file:
        config = json.load(file)
    return config

def check_in():
    print("Place Holder")

# ##Job Actions
def choosemodule(job_data):
    if job_data.module == "steno":
        stenoquery()
    return

def runpulledpork():  # Reruns pulledpork, adding any new rules.
    return()


def stenoquery():  # Queries stenographer, returning results in html/json
    subprocess.run("/opt/pulledpork/pulledpork.sh")
    return()


while True:
    job_board()

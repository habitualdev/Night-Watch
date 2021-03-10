import subprocess

def get_job():
    # Exists to query the job board for stuff to do
    job= ""
    return job


def run_job():  # Queueing service to run jobs
    return()


def push_results():  # Returns job results to the job board
    return()


def choosemodule(job_data):
    if job_data.module == "steno":
        stenoquery()
    return


def runpulledpork():  # Reruns pulledpork, adding any new rules.
    return()


def stenoquery():  # Queries stenographer, returning results in html/json
    subprocess.run("/opt/pulledpork/pulledpork.sh")
    return()
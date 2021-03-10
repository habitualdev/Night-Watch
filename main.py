# #Modular python server/client framework for Night Owl##
# #IMPORTS
import json
import server

# #Classes

json_job_template={
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

json_watchman_config = {
  "watchman": {
    "server": {
      "addr": "127.0.0.1",
      "port": "5000",
      "pollinterval": "5",
      "authkey": "STATIC_KEY"
    },
    "modules": {
      "steno": "true",
      "pulledpork": "true",
      "splunk": "true"
    }
  }
}

json_jobboard_config = {
  "job_board": {
    "api": {
      "addr": "127.0.0.1",
      "port": "5000",
      "loglevel": "error",
      "logfile": "/opt/nightwatch/log/api.log"
    },
    "authkey": "STATIC_KEY"
  }
}


# ##Command and control functions###

apikey = "TEST"


def get_role():  # Tells if host is a job board or watchman
    filename = "watch.json"
    with open(filename, "ro") as file:
        config = json.load(file)
    return config


def check_in():
    print("Place Holder")


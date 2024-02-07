import os
import sys
import json
import requests

class Task:
    def __init__(self, data):
        self.name = data["name"]

class TaskFetcher:
    def __init__(self):
        try:
            self.url = os.environ["CHORES_API_URL"]
        except KeyError:
            print("Missing required envar: CHORES_API_URL")
            sys.exit(1)

    def fetch_overdue_tasks(self):
        tasks = json.loads(self.fetch_json())
        return [Task(data) for data in tasks]

    def fetch_json(self):
        # Bit of a hack for dev/testing, if the api url is a file just load the json response from that file
        if os.path.isfile(self.url):
            return self.json_from_file(self.url)
        else:
            return self.json_from_api()

    def json_from_file(self, path):
        with open(path) as file:
            return file.read()

    def json_from_api(self):
        endpoint_url = f"{self.url}/api/tasks/overdue"
        response = requests.get(endpoint_url)
        if response.status_code != 200:
            raise Exception(f"Error fetching tasks from api {endpoint_url}. Got status code {response.status_code}")
        return response.text

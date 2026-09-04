from util import api_url

import os
import json
import requests
from requests.adapters import HTTPAdapter, Retry

class Task:
    def __init__(self, data):
        self.name = data["name"]
        self.overdue_text = data["overdueText"]

class TaskFetcher:
    def __init__(self):
        self.url = api_url()

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

        session = requests.Session()
        # This will only retry connection failures, if you want to retry on certain HTTP status codes you should
        # supply the status_forcelist parameter
        retries = Retry(
            total=3,
            backoff_factor=0.1,
        )
        session.mount('', HTTPAdapter(max_retries=retries))
        
        response = session.get(endpoint_url)
        
        if response.status_code != 200:
            raise Exception(f"Error fetching tasks from api {endpoint_url}. Got status code {response.status_code}")
        return response.text

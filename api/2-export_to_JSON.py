#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file using a REST API."""
import json
import sys
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(url):
    """Fetch a URL and return the parsed JSON."""
    request = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user = get_json("{}/users/{}".format(BASE_URL, employee_id))
    todos = get_json("{}/todos?userId={}".format(BASE_URL, employee_id))

    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": user.get("username")} for task in todos]

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)

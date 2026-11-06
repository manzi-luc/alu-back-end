#!/usr/bin/python3
"""Gather TODO list progress for an employee using a REST API."""
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

    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))

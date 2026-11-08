#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file using a REST API."""
import csv
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

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id,
                             user.get("username"),
                             task.get("completed"),
                             task.get("title")])

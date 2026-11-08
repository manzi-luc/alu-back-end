#!/usr/bin/python3
"""Export all employees' TODO lists to a JSON file using a REST API."""
import json
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(url):
    """Fetch a URL and return the parsed JSON."""
    request = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    users = get_json("{}/users".format(BASE_URL))
    todos = get_json("{}/todos".format(BASE_URL))

    all_tasks = {}
    for user in users:
        all_tasks[str(user.get("id"))] = [
            {"username": user.get("username"),
             "task": task.get("title"),
             "completed": task.get("completed")}
            for task in todos if task.get("userId") == user.get("id")]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)

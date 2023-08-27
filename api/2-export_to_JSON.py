#!/usr/bin/python3
""" Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = todo_response.json()

    for key, value in employee_data.items():
        if key == "id":
            USER_ID = value
        if key == "username":
            USERNAME = value

    json_filename = f"{USER_ID}.json"

    """ Creates an empty list where it will store in each iteration,
    a dictionary with the tasks and their status. """
    tasks_list = []
    for task in todo_data:
        TASK_TITLE = task['title']
        TASK_COMPLETED_STATUS = task['completed']
        tasks_list.append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME})

    """ Dictionary with the user id as key and a list as value. """
    data_to_export = {USER_ID: tasks_list}

    with open(json_filename, 'w') as f:
        json.dump(data_to_export, f)

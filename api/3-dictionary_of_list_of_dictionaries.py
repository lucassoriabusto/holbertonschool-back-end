#!/usr/bin/python3
""" Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress."""

import json
import requests
import sys


if __name__ == "__main__":

    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users")
    employee_data = response.json()

    data_to_export = {}

    for user_data in employee_data:
        USER_ID = user_data['id']
        USERNAME = user_data['username']

        todo_response = requests.get(
                f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}")
        todo_data = todo_response.json()

        tasks_list = []
        for task in todo_data:
            TASK_TITLE = task['title']
            TASK_COMPLETED_STATUS = task['completed']
            tasks_list.append({
                "username": USERNAME,
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS})

        data_to_export[USER_ID] = tasks_list

    json_filename = "todo_all_employees.json"

    with open(json_filename, 'w') as f:
        json.dump(data_to_export, f)

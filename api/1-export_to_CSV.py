#!/usr/bin/python3
""" Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress."""

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

    """USER_ID = employee_data.get('id')
    USERNAME = employee_data.get('username')"""

    csv_filename = f"{USER_ID}.csv"

    with open(csv_filename, 'w') as csvfile:
        for task in todo_data:
            TASK_TITLE = task['title']
            TASK_COMPLETED_STATUS = task['completed']
            data_to_write = (f'"{USER_ID}","{USERNAME}",\
"{TASK_COMPLETED_STATUS}","{TASK_TITLE}"')
            csvfile.write(data_to_write + '\n')

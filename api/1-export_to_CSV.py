#!/usr/bin/python3
""" """

import requests
import sys
import csv


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = 0
    completed_task_titles = []

    for task in todo_data:
        if task["completed"]:
            completed_tasks += 1
            completed_task_titles.append(task["title"])

    print(f"Employee {employee_data['name']} "
          f"is done with tasks({completed_tasks}/{total_tasks}):")

    for task in completed_task_titles:
        print(f"\t {task}")

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

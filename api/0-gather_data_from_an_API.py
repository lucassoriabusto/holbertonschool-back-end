#!/usr/bin/python3
""" Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = 0
    for task in todo_data:
        if task['completed']:
            completed_tasks += 1

    print(f"Employee {employee_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task["completed"]:
            print("\t", task["title"])

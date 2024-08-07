#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(employee_id)).json()

    user_response = requests.get(url + "users/{}".format(employee_id))

    user = user_response.json()

    params = {"userId": employee_id}

    todos_response = requests.get(url + "todos", params=params)

    todos = todos_response.json()

    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), len(completed), len(todos)))
    for complete in completed:
        print("\t {}".format(complete))

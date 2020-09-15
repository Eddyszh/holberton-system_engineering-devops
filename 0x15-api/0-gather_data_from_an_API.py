#!/usr/bin/python3
"""for a given emplyee id, returns information
    about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    """Returns todo list"""
    uid = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(uid)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(uid)).json()
    tasks = []
    for task in todo:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{})".
          format(user.get('name'), len(tasks), len(todo)))
    for task in tasks:
        print("\t {}".format(task))

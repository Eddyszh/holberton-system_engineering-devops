#!/usr/bin/python3
"""Python script to export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Records all tasks that are owned by the employee"""
    uid = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(uid)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(uid)).json()
    uname = user.get('username')
    tasks = []
    for task in todo:
        t_dict = {}
        t_dict['task'] = task.get('title')
        t_dict['completed'] = task.get('completed')
        t_dict['username'] = uname
        tasks.append(t_dict)
    js_dict = {}
    js_dict[uid] = tasks
    with open("{}.json".format(uid), 'w') as jsfile:
        json.dump(js_dict, jsfile)

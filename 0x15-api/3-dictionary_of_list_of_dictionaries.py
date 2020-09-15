#!/usr/bin/python3
"""Python script to export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Records all tasks from all employees"""
    users = requests.get('https://jsonplaceholder.typicode.com/users',
                         verify=False).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        verify=False).json()
    udict = {}
    unamedict = {}
    for user in users:
        id = user.get('id')
        udict[id] = []
        unamedict[id] = user.get('username')
    for task in todo:
        t_dict = {}
        id = task.get('userId')
        t_dict['task'] = task.get('title')
        t_dict['completed'] = task.get('completed')
        t_dict['username'] = unamedict.get(id)
        udict.get(id).append(t_dict)
    with open('todo_all_employees.json', 'w') as jsfile:
        json.dump(udict, jsfile)

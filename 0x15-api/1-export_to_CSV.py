#!/usr/bin/python3
"""export data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Records all tasks that are owned by the employee"""
    uid = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(uid)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(uid)).json()
    with open("{}.csv".format(uid), 'w') as csvf:
        writer = csv.writer(csvf, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([uid, user.get('username'),
                            task.get('completed'), task.get('title')])

#!/usr/bin/python3
"""Extends the 0-gather_data_from_an_API to export data in json format"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    user_page = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".
            format(argv[1])).json()
    todo_page = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".
            format(argv[1])).json()
    username = user_page.get("username")
    user_id = argv[1]

    tasks = []
    for task in todo_page:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
        todos = {}
        todos[user_id] = tasks
        with open("{}.json".format(user_id), 'w') as jsonfile:
            json.dump(todos, jsonfile)

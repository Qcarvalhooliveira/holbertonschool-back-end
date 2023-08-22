#!/usr/bin/python3
"""export employees's todo list progress"""

import json
import requests

if __name__ == '__main__':
    user_info = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    user_tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    userdict = {}
    usernamedict = {}

    for user in user_info:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")

    for task in user_tasks:
        taskdict = {}
        uid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)

#!/usr/bin/python3
"""export employees's todo list progress"""

import json
import requests

if __name__ == '__main__':
    users_page = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    todo_page = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    userdict = {}
    usernamedict = {}

    for user in users_page:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")

    for task in todo_page:
        taskdict = {}
        uid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)
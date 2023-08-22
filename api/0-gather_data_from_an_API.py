#!/usr/bin/python3
"""For a given employee ID, returns information about his/her
   TODO list progress."""

import requests
from sys import argv


if __name__ == '__main__':
    user_page = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(argv[1])).json()
    todo_page = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(argv[1])).json()
    titles = []
    for task in todo_page:
        if task.get('completed') is True:
            titles.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user_page.get('name'), len(titles), len(todo_page)))
    print("\n".join("\t {}".format(task) for task in titles))

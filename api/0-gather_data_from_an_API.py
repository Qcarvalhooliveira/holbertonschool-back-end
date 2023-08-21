#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her TODO list progress.
'''

import requests
from sys import argv


if __name__ == '__main__':
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                             format(argv[1])).json()

    user_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.
        format(argv[1])).json()
    titles = []

    for tasks in user_tasks:
        if tasks.get('completed') is True:
            titles.append(tasks.get('title'))

    print('Employee {} is done with tasks({}/{}):'.
          format(user_info.get('name'), len(titles), len(user_info))),

    print('\n'.join('\t {}'.format(task) for task in titles))

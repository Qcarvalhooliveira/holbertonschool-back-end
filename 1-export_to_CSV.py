#!/usr/bin/python3
"""For a given employee ID, returns information about his/her TODO list progress."""

import csv
import sys
import requests

if __name__ == '__main__':
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    USER_ID = sys.argv[1]
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                             format(USER_ID)).json()

    EMPLOYEE_NAME = user_info['username']

    user_tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                              format(USER_ID)).json()

    with open(USER_ID + '.csv', 'w', newline='') as csv_file:
        write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            write.writerow([USER_ID, EMPLOYEE_NAME,
                            task['completed'], task['title']])

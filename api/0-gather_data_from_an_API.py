#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her TODO list progress.
'''

import sys
import requests

if __name__ == '__main__':
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    
    USER_ID = sys.argv[1]
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(USER_ID)).json()
    
    EMPLOYEE_NAME = user_info.get("username")
    user_tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(USER_ID)).json()
    for tasks in user_tasks:
        if tasks.get('completed') is True:
            TASK_TITLE.append(tasks.get('title'))
            NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_DONE_TASKS = len(user_tasks)

    print('Employee {} is done with tasks({}/{}):'.
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_DONE_TASKS))
    for title in TASK_TITLE:
        print('\t {}'.format(title))

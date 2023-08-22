#!/usr/bin/python3
"""Extends the 0-gather_data_from_an_API to export data in CSV format"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(argv[1])).json()
    user_tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(argv[1])).json()

    with open("{}.csv".format(argv[1]), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            csv_writer.writerow([int(argv[1]), user_info.get('username'),
                                 task.get('completed'),
                                 task.get('title')])

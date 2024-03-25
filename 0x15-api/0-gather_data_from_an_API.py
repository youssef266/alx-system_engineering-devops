#!/usr/bin/env python3
"""Gather data from an API"""
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Make a GET request to retrieve employee information
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
employee_data = response.json()

# Make a GET request to retrieve employee's TODO list
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
todos = response.json()

# Filter completed tasks
completed_tasks = [todo for todo in todos if todo['completed']]

# Display employee TODO list progress
print(f"Employee {employee_data['name']} is done with tasks({len(completed_tasks)}/{len(todos)}):")
for task in completed_tasks:
    print(f"\t{task['title']}")

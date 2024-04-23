#!/usr/bin/python3
"""
a python script that, using a specific REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import sys
import requests

def get_todo_list_progress(employee_id):
    # Base URL of the REST API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Endpoint for fetching user data
    user_endpoint = f'{base_url}/users/{employee_id}'

    # Endpoint for fetching user's todo list
    todo_endpoint = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch user data
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()
        employee_name = user_data['name']

        # Fetch user's todo list
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        # Count completed tasks
        completed_tasks = [task for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_data)

        # Display progress
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Ensure employee ID is an integer
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_todo_list_progress(employee_id)

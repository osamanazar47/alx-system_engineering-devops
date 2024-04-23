#!/usr/bin/python3
"""
a python script that, using a specific REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def get_todo_list_progress(employee_id):
    """A function for fetching data from the REST API"""
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
        name = user_data['name']

        # Fetch user's todo list
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        # Count completed tasks
        completed_t = [task for task in todo_data if task['completed']]
        len_of_com = len(completed_t)
        total_t = len(todo_data)

        # Display progress
        print(f"Employee {name} is done with tasks({len_of_com}/{total_t}):")
        for task in completed_t:
            print(f"\t {task['title']}")

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

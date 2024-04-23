#!/usr/bin/python3
"""
a python script that, using a specific REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


def get_todo_list_progress():
    """A function for fetching data from the REST API"""
    # Base URL of the REST API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Endpoint for fetching user data
    user_endpoint = f'{base_url}/users'

    try:
        # Fetch user data
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()

        json_data = {}
        for user in user_data:
            user_id = user["id"]
            username = user["username"]
            todos = requests.get(f'{base_url}/todos?userId={user_id}').json()
            user_tasks = [{
                "task": todo["title"],
                "completed": todo["completed"],
                "username": username
            } for todo in todos]
            json_data[user_id] = user_tasks

        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(json_data, jsonfile)

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.exit(1)
    get_todo_list_progress()

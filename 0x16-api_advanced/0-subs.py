#!/usr/bin/python3
"""a python script for querying the Reddit API"""
import requests

def number_of_subscribers(subreddit):
    """a function that returns the number of subscribers for
    a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={"User-Agent": "Python Script"})

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0  # Return 0 if the subreddit doesn't exist or there's an error



if __name__ == '__main__':
    number_of_subscribers()

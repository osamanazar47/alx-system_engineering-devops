#!/usr/bin/python3
"""a python script for querying the Reddit API"""
import requests


def top_ten(subreddit):
    """a function that returns the top 10  hot posts for
    a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get('data')
        [print(post.get('data').get('title')) for post in posts.get('children')]
    else:
        return ('None')  # Return 0 if the subreddit doesn't exist or there's an error

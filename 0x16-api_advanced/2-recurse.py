#!/usr/bin/python3
"""a recursive function for querying from reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    """
    params = {"limit": 100}
    if after:
        params["after"] = after

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python Script"}

    response = requests.get(url, params=params,
                            headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    if not posts:
        return hot_list

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

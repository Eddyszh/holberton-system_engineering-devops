#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    subs = requests.get(url, headers=header, allow_redirects=False).json()
    if "data" in subs:
        return subs.get("data").get("subscribers")
    else:
        return 0

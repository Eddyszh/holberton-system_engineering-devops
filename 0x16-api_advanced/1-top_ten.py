#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Returns the top 10 hot posts"""
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    posts = requests.get(url, headers=header, allow_redirects=False).json()
    if "data" in posts:
        for post in posts.get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)

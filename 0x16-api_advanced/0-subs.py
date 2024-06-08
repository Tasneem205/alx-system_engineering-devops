#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import json
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; CustomBot/0.1)'}
    if subreddit is None or type(subreddit) is not str:
        return (0)
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                     headers=headers)
    data = r.json()
    if r:
        return data['data']['subscribers']
    else:
        return (0)

#!/usr/bin/python3
"""
number of followers to a subreddit
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ return the number of sunscribbers to a subreddit """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; CustomBot/0.1)'}
    if subreddit is None or type(subreddit) is not str:
        return (0)
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                     headers=headers)
    data = r.json()
    if r:
        return r.get("data", {}).get("subscribers", 0)
    else:
        return (0)

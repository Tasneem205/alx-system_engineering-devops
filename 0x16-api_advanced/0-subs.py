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
        print("subreddit is none or not a string")
        return (0)
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                     headers=headers)
    data = r.json()
    if r:
        return data['data']['subscribers']
    else:
        print("request is not defined")
        return (0)

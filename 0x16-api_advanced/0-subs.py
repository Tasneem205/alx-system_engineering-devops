#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    headers = {'User-Agent': 'MyRedditApp/0.1 (by u/YourRedditUsername)'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx and 5xx)

        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)

        return subscribers

    except requests.exceptions.RequestException:
        return 0
"""    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "MyRedditApp/0.1 (by tasneemabdeltawab205@gmail.com)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
"""

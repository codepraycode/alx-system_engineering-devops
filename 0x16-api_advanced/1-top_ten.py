#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


API_URL = "https://www.reddit.com/r/{}/hot/.json"


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = API_URL.format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/cpc)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]

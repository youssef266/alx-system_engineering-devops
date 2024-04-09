#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid"""
    headers = {'User-Agent': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzEyNzcxNjc4LjQxMjE3MywiaWF0IjoxNzEyNjg1Mjc4LjQxMjE3MiwianRpIjoiU3hMQ0N3WHNHU1pnVTNsVV9MdmpMQnotVGNKeVR3IiwiY2lkIjoiN2xWWFlJWVpGQzRiVTEtRW04NTRRQSIsImxpZCI6InQyXzVqYmFtZm5zZSIsImFpZCI6InQyXzVqYmFtZm5zZSIsImxjYSI6MTY3NjgzNTA3MTAwMCwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.lXu6bFbr8stG9u1k4GzUAqCeYOCUtMPeOkQBB9mIbT6fCiaVN2SeTKlO-jWQsXY26pjS8k3cMINL6JjsqkV0bkphdKajsG-VZ6M_Jzl9VaXPD8sfS0rz_U81OyqBuU54pfDckJXPBDNCq9KpxFuxaMBFu7rq51cGOnblcp2eYznBz89f6zpwd1VpAxHNWjup_68QQj2k4GMIMAAeQNZ4lp6Q4BQvxRLYlhzFq44wn_8HAaQa2D7eaSHUkuqO1KC7dfm4jFjpY_cvAmqGRvCMONsDzYcPav_YzYdkagavjlPgsm5-eHNzUBn3yZ4FYiELnun2tIOwrjNAycaMMeI45Q'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)

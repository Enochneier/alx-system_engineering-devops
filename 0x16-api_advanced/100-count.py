#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon 15 Apr 2024

@author: Enochneier
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    data = response.json()

    if 'error' in data or 'data' not in data:
        return

    posts = data['data']['children']
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())

    if data['data']['after']:
        return count_words(subreddit, word_list, data['data']['after'], counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")


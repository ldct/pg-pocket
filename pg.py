#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

#t = requests.get("http://www.paulgraham.com/articles.html").text
with open("Essays.html") as f:
  t = f.read()
soup = BeautifulSoup(t)
links = [link.get('href') for link in soup.find_all('a')]
links = [l for l in links if l[:26] == "http://www.paulgraham.com/" and l[26:] not in ["index.html", "rss.html"]]
for l in links:
  print(l[26:])
  with open(l[26:]) as f:
    if len(f.readlines()) > 5:
      continue
  with open(l[26:], 'w') as f:
    t = requests.get(l).text
    f.write(t)

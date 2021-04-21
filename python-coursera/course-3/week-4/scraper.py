import urllib.request, urllib.parse, urlib.error
from bs4 import BeautifulSoup

url = input()
html = urlib.request.urlopen().read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
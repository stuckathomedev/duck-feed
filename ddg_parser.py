import requests
from lxml import html

uquery = input("Search Query: ")
r = requests.get("https://duckduckgo.com/html/?q=" + uquery)

tree = html.fromstring(r.content)

links = tree.xpath('//a[@class="result__url"]/@href')

print("Links: ", links)
import requests
from lxml import html

uquery = input("Search Query: ")
r = requests.get("https://duckduckgo.com/html/?q=" + uquery, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

tree = html.fromstring(r.content)

links = tree.xpath('//h2[@class="result__title"]/a[@class="result__a"]/@href')

print("Links: ", links)
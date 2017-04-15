import requests
from lxml import html

def scrapeWeb(website):
    r = requests.get(website)

    tree = html.fromstring(r.content)
    rss_link = tree.xpath('//link[@rel="alternate" and @type="application/atom+xml"]/@href')

    return rss_link

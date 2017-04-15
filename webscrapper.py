import requests
import urllib
from lxml import html

class NoLinkError(Exception):
    pass

def scrape_web(website):
    r = requests.get(website)

    tree = html.fromstring(r.content)
    rss_links = tree.xpath('//link[@rel="alternate" and @type="application/atom+xml"]/@href')

    if len(rss_links) == 0:
        raise NoLinkError(website)
    else:
        return urllib.parse.urljoin(website, rss_links[0])

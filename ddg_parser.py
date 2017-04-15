import urllib

import requests
from lxml import html

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'


def get_links(query):
    urlencoded_query = urllib.parse.quote_plus(query)
    r = requests.get("https://duckduckgo.com/html/?q=" + urlencoded_query,
                     headers={'User-Agent': USER_AGENT})

    tree = html.fromstring(r.content)

    return tree.xpath('//h2[@class="result__title"]/a[@class="result__a"]/@href')
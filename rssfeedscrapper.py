import feedparser


def rssScrape(feed):
    rss_feed = feedparser.parse(feed)
    return rss_feed

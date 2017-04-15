import feedparser


def scrape_rss(feed):
    rss_feed = feedparser.parse(feed)
    return rss_feed

import json


class FeedManager:
    def __init__(self):
        # load feeds
        with open('feeds.json') as feed_data:
            d = json.load(feed_data)
            self.sub_feeds = d

    # Appends new feeds to the list taken from JSON
    def append_feed(self, feed):
        if feed not in self.sub_feeds:
            self.sub_feeds.append(feed)
        print(self.sub_feeds)

    def remove_feed(self, feed):
        if feed in self.sub_feeds:
            self.sub_feeds.remove(feed)
        print(self.sub_feeds)

    def get_feeds(self):
        return self.sub_feeds

    # Overrides current text in JSON file, and updates with new list
    def update_json(self):
        with open('feeds.json', mode='w', encoding='utf-8') as feeds_file:
            json.dump(self.sub_feeds, feeds_file)
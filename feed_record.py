import json


# Loads the list of subscribed reddit feeds from JSON file
def load_feeds():
    with open('feeds.json') as feed_data:
        d = json.load(feed_data)
        return d


# Appends new feeds to the list taken from JSON
def append_feeds(feed):
    sub_feeds.append(feed)


# Overrides current text in JSON file, and updates with new list
def update_json():
    with open('feeds.json', mode='w', encoding='utf-8') as feedsjson:
        json.dump(sub_feeds, feedsjson)


# Calls functions
user_feed = input("FEED: ")

sub_feeds = load_feeds()
append_feeds(user_feed)
update_json()
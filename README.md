## Duck Feed

### What is Duck Feed?

Duck feed is an desktop application that allows you to scrape the web looking for RSS feeds, subscribe to them, download them, and read them online or offlines. The application also even has a built in web browser for easier flow. 

### What was it made for?

This application was made for Hack Exeter Spring 2017! Our team name was _The Mighty Ducks_ and we won an award! We won the _developers award_ which was awarded for highest proficiency and skill. A full summary is available on the hack exeter [website](http://www.hackexeter.com/2017-spring.html)!

### Why DuckDuckGo

Common question! It's actually really simple! There are 2 reasons we decided to use DuckDuckGo:
1. Privacy: DuckDuckGo is famous for not taking information and data from users
2. DuckDuckGo: Easier to parse. Google and other search engines super optimze their searches making it very difficult to parse.

DuckDuckGo isn't all fun and rainbows though. DuckDuckGo's search results are not that accurate and useful as other search engines. We hope to find a solution to some of these issues in the future. 

### How does it work?

It's actually a lot simpler than you think! We use 3 web scrapers. First we take the input from the user which is just the search keyword. We then add that string to the search link for DuckDuckGo, which looks like this `https://duckduckgo.com/html/?q=`. This will give the list of search results. If you actually go to that link with the keywords added to the end you'll see the normal search results. For example if the user enters `cats`, the link would be `https://duckduckgo.com/html/?q=cats`. Originally we were going to use the DuckDuckGo API to search and get results but it was not updated for Python 3. 

Anyways, our second scraper goes through the resulting search results. The HTML from the search results is given from the first scraper to the second scraper. The second scraper looks for link to the websites. To do this, we used _XPath_. We specified a search query. Our search queries looked like this `//h2[@class="result__title"]/a[@class="result__a"]/@href`. This searches for `h2` tags with the `result__title` class and `a` tags with the `result__a` class and returns the attribute value for the `href` attribute, if there, which is the link. It also returns what is in between the tags.

We then put this through _another_ scraper which scrapes for *RSS Feeds*. We do this by once again using _XPath_. With this links returned by the second scraper, we scrape the website and submit an XPath query that searches for `link` tags with a certain `rel`  and `type` attributes. The entire query is `//link[@rel="alternate" and @type="application/atom+xml"]/@href`. This works as described before and searches for `rel` tags with `"alternate"` and `"application/atom+xml"` and returns the link in the `href` attribute. We then have one more step

We then parse the RSS Feed link which was return from the previous scraper if it was found. This is pretty simple. No seriously. It's only 4 lines. I'll put all of the code below
```python
import feedparser


def scrape_rss(feed):
    rss_feed = feedparser.parse(feed)
    return rss_feed
```
There isn't much to explain for this one. You enter what is returned from the previous scraper and it returns everything about the RSS feed. Posts, titles, subtitles, etc. That's pretty much done. I'm not going to go in depth about glade and GTK but I'll quickly explain how we are saving user subscriptions. 

First, we initialize the feedmanager with the `__init__` function, which is below:
```python
with open('feeds.json') as feed_data:
            d = json.load(feed_data)
            self.sub_feeds = d
```
This loads all of the feeds that are stored in the JSON file. Next we define a couple methods which allow us to append, remove, return feeds, and update the JSON file. To Append and Remove, we have to edit the python list and convert it to a JSON list, the code for which is below:
```python
def append_feed(self, feed):
        if feed not in self.sub_feeds:
            self.sub_feeds.append(feed)
        print(self.sub_feeds)

    def remove_feed(self, feed):
        if feed in self.sub_feeds:
            self.sub_feeds.remove(feed)
        print(self.sub_feeds)
```
The print is not significat but were used for us to make sure it was functioning properly. Finally, we have a method that updates the JSON file, which is below:
```python
def update_json(self):
        with open('feeds.json', mode='w', encoding='utf-8') as feeds_file:
            json.dump(self.sub_feeds, feeds_file)
```

Everything else is much more complicated and will take up too much space to explain. Sorry! Hope you learned something.

### Current Issues

The application is facing a couple issues preventing it from being released. If you have a solution, feel free to contribute!
 - **Security**: This application does not use any sort of account, but the graphical library used in this application, GTK, has some security issues that may compropmise. Until this is fixed, for saftey, there will be no releases
 - **Multi-Platform**: The application has not yet been test for windows or mac systems due to issues with GTK during development. Minor issue

### Installation

**Prerequisites**
- ` Python 3+`
- `GTK+`
- `WebKitGTK+`
- `feedparser`
- `urllib`
- `requests`
- `lxml`
- `json`

**Running**
```markdown
~ python __main__.py
```
_NOTE: You may have issues running this on windows until issues listed above are fixed_

### Easter Eggs

So, you're looking for easter eggs? Well you're not in luck. Why don't you ask duck feed itself? Just type in `Easter Eggs` in _DuckDuckGo search_ and you'll get an answer. Or why don't you try and search the glourious school `Phillips Exeter`?

## Duck Feed

### What is Duck Feed?

Duck feed is an desktop application that allows you to scrape the web looking for RSS feeds, subscribe to them, download them, and read them online or offlines. The application also even has a built in web browser for easier flow. 

### What was it made for?

This application was made for Hack Exeter Spring 2017! Our team name was _The Mighty Ducks_ and we won an award! We won the _developers award_ which was awarded for highest proficiency and skill. A full summary is available on the hack exeter [website](http://www.hackexeter.com/2017-spring.html)!

### How does it work?

It's actually a lot simpler than you think! We use 3 web scrapers. First we take the input from the user which is just the search keyword. We then add that string to the search link for DuckDuckGo, which looks like this `https://duckduckgo.com/html/?q=`. This will give the list of search results. If you actually go to that link with the keywords added to the end you'll see the normal search results. For example if the user enters `cats`, the link would be `https://duckduckgo.com/html/?q=cats`. Originally we were going to use the DuckDuckGo API to search and get results but it was not updated for Python 3. 

Anyways, our second scraper goes through the resulting search results. The HTML from the search results is given from the first scraper to the second scraper. The second scraper looks for link to the websites. To do this, we used _XPath_. We specified a search query. Our search queries looked like this `//h2[@class="result__title"]/a[@class="result__a"]/@href`. This searches for `h2` tags with the `result__title` class and `a` tags with the `result__a` class and returns the attribute value for the `href` attribute, if there, which is the link. It also returns what is in between the tags.

We then put this through _another_ scraper which scrapes for *RSS Feeds*

### Current Issues

The application is facing a couple issues preventing it from being released. If you have a solution, feel free to contribute!
 - **Security**: This application does not use any sort of account, but the graphical library used in this application, GTK, has some security issues that may compropmise. Until this is fixed, for saftey, there will be no releases
 - **Multi-Platform**: The application has not yet been test for windows or mac systems due to issues with GTK during development. Minor issue

### Installation

**Prerequisites**
- ` Python 3+`
- `GTK+`
- `WebKitGTK+`
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

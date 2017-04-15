import requests
from html.parser import HTMLParser
from html.entities import name2codepoint

# Gets user search query
uquery = input("Search Query: ")

# Submits query to Duck Duck Go
r = requests.get("https://duckduckgo.com/?q=" + uquery)
log = open("testlog.txt", "w+")
log.write(r.text)
log.close()

# DuckDuckGo HTML Parser
class ddg_parser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        print("stag: ", tag)
        for attr in attrs:
            print("attr: ", attr)

    def handle_endtag(self, tag):
        print("etag:")

    def handle_data(self, data):
        print("data: ", data)

    def handle_comment(self, data):
        print("comment: ", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("nnet: ", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("nu ent: ", c)

    def handle_decl(self, data):
        print("Decl: ", data)

parser = ddg_parser







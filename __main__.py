import threading
import signal
from ddg_parser import get_links
from webscrapper import scrape_web, NoLinkError
from rssfeedscrapper import scrape_rss

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


class Handler:
    def __init__(self, builder):
        self.ddg_query_box = builder.get_object('ddg_query_box')
        self.search_btn = builder.get_object('search_btn')
        self.output_box = builder.get_object('output_box')

        # Set up associations
        builder.get_object('menu').set_popover(builder.get_object('popover'))

    def print(self, text):
        self.output_box.set_text(self.output_box.get_text() + "\n" + text)

    def on_delete_window(*args):
        Gtk.main_quit(*args)

    def on_search_btn_pressed(self, button):
        ddg_query = self.ddg_query_box.get_text()
        if not ddg_query == "":

            def get_feeds_from_query():
                potential_feed_sites = get_links(ddg_query)
                for site in potential_feed_sites:
                    print("SITE: " + site)
                    try:
                        feed_link = scrape_web(site)
                    except NoLinkError:
                        continue

                    print("FEED LINK: " + feed_link)
                    feed = scrape_rss(feed_link)
                    print("FEED: " + str(feed))
                    GLib.idle_add(display_feed, feed)
                GLib.idle_add(reenable_controls)

            def display_feed(feed):
                self.print(feed["channel"]["title"])

            def reenable_controls():
                # Re-enable boxes
                self.ddg_query_box.set_sensitive(True)
                self.search_btn.set_sensitive(True)

            thread = threading.Thread(target=get_feeds_from_query)
            thread.daemon = True
            thread.start()
            # Disable boxes
            self.ddg_query_box.set_sensitive(False)
            self.search_btn.set_sensitive(False)
            print("Starting query async...")


def main():
    builder = Gtk.Builder()
    builder.add_from_file('window.glade')
    builder.connect_signals(Handler(builder))

    window = builder.get_object('window')
    window.show_all()

    # Fix keyboard interrupt not working
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()

if __name__ == '__main__':
    main()
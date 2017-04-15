import threading
import signal
import concurrent.futures
from ddg_parser import get_links
from web_scrapper import scrape_web
from rssfeed_scrapper import scrape_rss
from feed_manager import FeedManager

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


def process_site(site):
    print("SITE: " + site)
    try:
        feed_link = scrape_web(site)
        print("FEED LINK: " + feed_link)
        feed = scrape_rss(feed_link)
        return feed, feed_link
    except:
        print("Encountered error, returning nothing.")
        return None


class Handler:
    def __init__(self, builder, feed_manager):
        self.feed_manager = feed_manager
        self.ddg_query_box = builder.get_object('ddg_query_box')
        self.search_btn = builder.get_object('search_btn')
        self.feed_grid = builder.get_object('feed_grid')
        self.current_feed_grid_row = 2

        # Set up associations
        builder.get_object('menu').set_popover(builder.get_object('popover'))

    def on_sub_btn_clicked(self, btn, feed_link):
        if btn.get_active():
            self.feed_manager.append_feed(feed_link)
        else:
            self.feed_manager.remove_feed(feed_link)

    def on_delete_window(*args):
        Gtk.main_quit(*args)

    def on_search_btn_pressed(self, button):
        ddg_query = self.ddg_query_box.get_text()
        if not ddg_query == "":

            def get_feeds_from_query():
                potential_feed_sites = get_links(ddg_query)

                with concurrent.futures.ProcessPoolExecutor() as executor:
                    feed_tuples = executor.map(process_site, potential_feed_sites)
                    for feed_tuple in feed_tuples:
                        if feed_tuple is not None:
                            GLib.idle_add(display_feed, feed_tuple)
                    GLib.idle_add(reenable_controls)

            def display_feed(feed_tuple):
                feed = feed_tuple[0]
                feed_link = feed_tuple[1]
                sub_btn = Gtk.CheckButton()
                sub_btn.connect("toggled", self.on_sub_btn_clicked, feed_link)

                self.feed_grid.attach(sub_btn, 0, self.current_feed_grid_row, 1, 1)
                sub_btn.show()

                title_label = Gtk.Label(feed["channel"]["title"])
                self.feed_grid.attach(title_label, 1, self.current_feed_grid_row, 1, 1)
                title_label.show()

                desc_label = Gtk.Label(feed["channel"]["description"])
                self.feed_grid.attach(desc_label, 2, self.current_feed_grid_row, 1, 1)
                desc_label.show()

                self.current_feed_grid_row += 1

                print("Adding to box: ", feed_link)

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
    builder.connect_signals(Handler(builder, FeedManager()))

    window = builder.get_object('window')
    window.show_all()

    # Fix keyboard interrupt not working
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()

if __name__ == '__main__':
    main()
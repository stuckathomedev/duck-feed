import threading
import signal
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

from ddg_parser import get_links


class Handler:
    def __init__(self, builder):
        self.ddg_query_box = builder.get_object('ddg_query_box')
        self.search_btn = builder.get_object('search_btn')
        self.output_box = builder.get_object('output_box')

    def print(self, text):
        self.output_box.set_text(self.output_box.get_text() + "\n" + text)

    def on_delete_window(*args):
        Gtk.main_quit(*args)

    def on_search_btn_pressed(self, button):
        ddg_query = self.ddg_query_box.get_text()
        if not ddg_query == "":

            def get_rss_from_query():
                potential_rss_sites = get_links(ddg_query)
                GLib.idle_add(display_rss_results, str("moo"))
            def display_rss_results(rss):
                self.ddg_query_box.set_sensitive(True)
                self.search_btn.set_sensitive(True)

            thread = threading.Thread(target=get_rss_from_query)
            thread.daemon = True
            thread.start()
            self.ddg_query_box.set_sensitive(False)
            self.search_btn.set_sensitive(False)
            print("Starting query async...")

def main():
    builder = Gtk.Builder()
    builder.add_from_file('window.glade')
    builder.connect_signals(Handler(builder))

    window = builder.get_object('window')
    window.show_all()

    builder.get_object('menu').set_popover(builder.get_object('popover'))

    # Fix keyboard interrupt not working
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()

if __name__ == '__main__':
    main()
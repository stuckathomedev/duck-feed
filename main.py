
import signal
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def __init__(self):
        self.ddg_query_box = builder.get_object('ddg_query_box')
        self.output_box = builder.get_object('output_box')

    def print(self, text):
        self.output_box.set_text(self.output_box.get_text() + "\n" + text)

    def on_delete_window(*args):
        Gtk.main_quit(*args)

    def on_menu_pressed(*args):
        menu = builder.get_object('menu')
        print("menu pressed")
        menu.show_all()

    def on_search_btn_pressed(self, button):
        ddg_query = self.ddg_query_box.get_text()
        if not ddg_query == "":
            self.print("Query: " + ddg_query)

builder = Gtk.Builder()
builder.add_from_file('window.glade')
builder.connect_signals(Handler())

window = builder.get_object('window')
window.show_all()

signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
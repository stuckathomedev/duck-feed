import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Handler:
    def on_delete_window(*args):
        Gtk.main_quit(*args)

    def on_search_btn_pressed(self, button):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file('window.glade')
builder.connect_signals(Handler())

window = builder.get_object('window')
window.show_all()

Gtk.main()
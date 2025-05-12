import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ui import create_ui

if __name__ == "__main__":
    win = create_ui()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

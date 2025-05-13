import gi
from gi.repository import Gtk, GLib
from service_manager import get_services, manage_service

gi.require_version("Gtk", "3.0")

def on_action_clicked(button, service_lists, action):
    selected_row = None

    # Find the selected row in any of the service lists
    for listbox in service_lists.values():
        row = listbox.get_selected_row()
        if row:
            selected_row = row
            break

    if selected_row:
        service = selected_row.service_name
        parent = button.get_parent()
        status_label = parent.get_children()[0]
        status_message = manage_service(action, service)

        if isinstance(status_label, Gtk.Label):
            status_label.set_text(status_message)

        # Refresh all lists after a small delay to let systemd settle
        GLib.timeout_add(500, lambda: refresh_all_service_lists(service_lists))


def refresh_all_service_lists(service_lists):
    for filter_type, listbox in service_lists.items():
        populate_services(listbox, filter_type)
    return False  # Ensures the timeout only runs once

def populate_services(listbox, filter_type):
    listbox.foreach(lambda widget: listbox.remove(widget))
    services = get_services(filter_type)
    for service_name, status in services:
        row = Gtk.ListBoxRow()
        row.service_name = service_name
        row_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        label = Gtk.Label()
        label.set_text(f"{service_name} ({status})")
        label.set_xalign(0)
        label.set_margin_top(6)
        label.set_margin_bottom(6)
        label.set_margin_start(10)
        label.set_margin_end(10)
        row_box.pack_start(label, True, True, 0)
        row.add(row_box)
        listbox.add(row)
    listbox.show_all()
    listbox.queue_draw()

def create_action_buttons(service_lists):
    action_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
    actions = ['start', 'stop', 'restart', 'enable', 'disable']
    for action in actions:
        btn = Gtk.Button(label=action.capitalize())
        btn.connect("clicked", on_action_clicked, service_lists, action)
        action_buttons.pack_start(btn, True, True, 0)
    return action_buttons

def create_ui():
    win = Gtk.Window(title="Systemd Service Manager")
    win.set_border_width(10)
    win.set_default_size(800, 500)

    notebook = Gtk.Notebook()
    win.add(notebook)

    service_lists = {}  # Store each listbox keyed by its filter type

    for label, filter_type in [
        ("All Services", "all"),
        ("Running Services", "running"),
        ("Enabled at Boot", "enabled")
    ]:
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_margin_top(10)
        box.set_margin_bottom(10)
        box.set_margin_start(10)
        box.set_margin_end(10)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_vexpand(True)
        service_list = Gtk.ListBox()
        service_list.set_selection_mode(Gtk.SelectionMode.SINGLE)
        scrolled_window.add(service_list)
        box.pack_start(scrolled_window, True, True, 0)

        populate_services(service_list, filter_type)
        service_lists[filter_type] = service_list

        action_buttons = create_action_buttons(service_lists)
        box.pack_end(action_buttons, False, False, 0)

        notebook.append_page(box, Gtk.Label(label=label))

    return win

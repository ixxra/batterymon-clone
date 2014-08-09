'''
package notagir: Simple wrapper around pygtk, pyglib and pynotify to wrap them in Gtk3 syntax, as needed to share code between batterymon and batterymon-gtk3
'''

import gtk as Gtk
import glib as GLib

try:
    import pynotify as Notify
except:
    Notify = None


_oldMenu = Gtk.Menu


class _Menu(_oldMenu):
    def popup(self, parent_menu_shell, parent_menu_item, func, data, button, activate_time):
        _oldMenu.popup(self, parent_menu_shell, parent_menu_item, func, button, activate_time, data)
        

Gtk.Menu = _Menu


class GdkPixbuf:
    class Pixbuf:
        @classmethod
        def new_from_file_at_size(cls, filename, width, height):
            return Gtk.gdk.pixbuf_new_from_file_at_size(filename, width, height)


if Notify is not None:
    _oldNotification = Notify.Notification

    class _newNotification(_oldNotification):
        @classmethod
        def new(cls, summary, body):
            return _oldNotification(summary, body)


    Notify.Notification = _newNotification

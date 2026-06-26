import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
import subprocess

class DeviceManagerPage(Adw.PreferencesPage):
    def __init__(self):
        super().__init__(title="Device Manager")
        self.list_box = Gtk.ListBox()
        self.list_box.add_css_class("boxed-list")
        self.list_box.set_margin_start(20)
        self.list_box.set_margin_end(20)
        self.list_box.set_margin_top(20)
        
        group = Adw.PreferencesGroup(title="System Hardware", description="Connected PCIe and USB devices.")
        group.add(self.list_box)
        self.add(group)
        
        self.load_devices()

    def load_devices(self):
        try:
            # We assume your helper script is in /usr/bin
            result = subprocess.run(["lspci"], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if line:
                    row = Adw.ActionRow(title=line)
                    self.list_box.append(row)
        except Exception as e:
            self.list_box.append(Adw.ActionRow(title=f"Error loading devices: {str(e)}"))

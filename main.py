## DosBox APP

# IMPORTS
import random
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious

# KIVY Design
with open("main.kv") as kv:
    Builder.load_string(kv.read())

# App Class
class DoSBoX(App):

    def random_password(self, *args):
        words = "a1bc0UVWd4ehi2jklB3CDE6mGop5MNquvwFH8xyzAInJKLOP7fgQRSTXrstY9Z"
        Username = "DBuser" + str(random.randint(1000,9999))
        Password = "".join(random.choices(words, k=10))
        self.Password.text = Password
        self.Username.text = Username
        self.List += f"[b][color=#FF0000]USER: [color=#AAAAAA]{Username}\n[color=#FF0000]PASS: [color=#AAAAAA]{Password}[/color][/b]\n\n"
        self.ScrollView.ids.label.text = self.List

    # BUILD FUNCTION
    def build(self):

        # List
        self.List = ""

        # root
        self.root = FloatLayout(size_hint = (1, 1))
        
        # ActionBar
        self.ActionBar = ActionBar()

        # Scroll View
        self.ScrollView = ScrollView()
        self.ScrollView.ids.label.text = ""

        # Password
        self.Password = TextInput(pos_hint = {"right":0.95, "center_y":0.75})

        # Name
        self.Username = TextInput(pos_hint = {"right":0.95, "center_y":0.85})

        # Button
        self.Copy = Button(
            pos_hint = {"right":0.95, "center_y":0.07},
            text = "Copy",
            on_press = lambda _:Clipboard.copy(f"{self.Username.text}:{self.Password.text}")
            )

        # Add Widgets
        self.root.add_widget(self.ActionBar)
        self.root.add_widget(self.Username)
        self.root.add_widget(self.Password)
        self.root.add_widget(self.ScrollView)
        self.root.add_widget(self.Copy)

        # Clock
        Clock.schedule_interval((lambda _:self.random_password(self)), 2)        

        # RETRUN root       
        return self.root
# RUN
DoSBoX().run()
# -> END

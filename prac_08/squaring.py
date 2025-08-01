"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Lindsay Ward'

class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    output_text = StringProperty()  # Define a property to use with kv

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)  # Adjusted window size for new layout
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.output_text = str(result)
        except ValueError:
            self.output_text = "0.0"  # Set default value for invalid input

    def handle_clear(self):
        """ Clear input and output fields """
        self.root.ids.input_number.text = ''
        self.output_text = ''


SquareNumberApp().run()

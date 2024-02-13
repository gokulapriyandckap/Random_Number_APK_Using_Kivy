import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

# Ensure that the installed version of Kivy is at least 2.0.0
kivy.require('2.0.0')

# Define a custom layout class called MyRoot, which inherits from BoxLayout
class MyRoot(BoxLayout):
    def __init__(self):
        # Call the constructor of the parent class (BoxLayout)
        super(MyRoot, self).__init__()

    # Define a method to generate a random number and update the label text
    def generate_number(self):
        # Set the text of the random_label widget to a randomly generated number between 0 and 10000
        self.random_label.text = str(random.randint(0,10000))


# Define the main application class called RandomNumber, which inherits from the App class
class RandomNumber(App):
    # Define the build method, which is called when the application starts and returns the root widget
    def build(self):
        # Create an instance of the MyRoot class and return it as the root widget of the application
        return MyRoot()

# Create an instance of the RandomNumber class
random_number = RandomNumber()

# Run the Kivy application
random_number.run()

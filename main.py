from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty

class MainInterface(BoxLayout):
    inputed_data = StringProperty("0")

class OutputArea(BoxLayout):
    pass

class InputArea(BoxLayout):
    pass

class Top(BoxLayout):
    pass

class Middle(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for number in range(1,10):
            number_button = Button(
                                    text = str(number)
                            )
            self.add_widget(number_button)

class Right(BoxLayout):
    pass

class Bottom():
    pass

class CalcApp(App):
    pass

if __name__ == '__main__':
    CalcApp().run()
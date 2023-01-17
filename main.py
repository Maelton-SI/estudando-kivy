from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.properties import StringProperty


class MainInterface(GridLayout):
    count = 1
    unidades = StringProperty(str(count))

    def soma_unidade(self):
        self.count += 1
        self.unidades = str(self.count)
    
    def subtrai_unidade(self):
        self.count -= 1
        self.unidades = str(self.count)

class MyFirstApp(App):
    pass

if __name__ == '__main__':
    MyFirstApp().run()

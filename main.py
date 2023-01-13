from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainInterface(Widget):
    pass

class SecondInterface(Widget):
    pass

class MyFirstApp(App):
    pass

class ThirdInterface(BoxLayout):

    #Definições do construtor de interface pelo arquivo (.py)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Orientação dos objetos dentro da interface.
        self.orientation = "vertical"

        #Definindo elementos da interface.
        b1 = Button(
                text="One",
                color=(1,0,0,1)
            )
        
        b2 = Button(
                text="Two",
                color=(0,1,0,1)
            )
        
        b3 = Button(
                text="Three",
                color=(0,0,1,1)
            )

        #Adicionando elementos à interface.
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

class FourthInterface(BoxLayout):
    pass

class FifthInterface(BoxLayout):
    pass

class SixthInterface(BoxLayout):
    pass

class SeventhInterface(BoxLayout):
    pass

class EigthInterface(BoxLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class TenthInterface(AnchorLayout):
    pass

#class GridLayoutExample(GridLayout):
    #pass
    
    #Essa classe foi definida dentro do arqivo (.kv)

if __name__ == '__main__':
    MyFirstApp().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp

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

'''
#Essa classe foi definida a partir do arquivo (.kv)
class GridLayoutExample(GridLayout):
    pass
'''

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Valores possíveis para a propriedade orientation (forma com que os elementos são inseridos e exibidos na interface) em um StackLayout:
        #"lr-tb" (left-right, top-bottom)
        #"rl-tb" (right-left, top-bottom)
        #"lr-bt" (left-right, bottom-top)
        #"rl-bt" (left-right, bottom-top)
        self.orientation = "lr-tb"
        
        #A propriedade padding determina o espaçamento interno da interface em relação a seus elementos.
        #padding: width, height
        self.padding = dp(20), dp(100)

        self.spacing = 5

        for button in range(1, 82):
            b = Button(
                        text = str(button), 
                        size_hint = (.1, .1)
                    )

            self.add_widget(b)
        
        for letra in 'ABCDEFG':
            b = Button(
                        text = str(letra),
                        size_hint = (None, None),
                        size = (dp(50), dp(50))
            )

            self.add_widget(b)

class TwelvethInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        b = Label(
                    text = "Serei o primeiro a ser inserido na tela, antes dos elementos definidos no arquivo (.kv)."
                )
        
        self.add_widget(b)

class ThirteenthInterface(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for button in range(1, 82):
            b = Button(
                        text = str(button),
                        size_hint = (None, None),
                        size = (dp(100), dp(100))
                )
            
            self.add_widget(b)

if __name__ == '__main__':
    MyFirstApp().run()
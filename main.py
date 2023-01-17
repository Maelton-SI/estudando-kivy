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
    #Tendo em vista que as configurações gráficas foram definidas no arquivo (.kv) não se faz necessária a definição do construtor da classe.

    possibilities = [["Modify label", "Modify me!"], ["Unmodify label", "Umodify me!"]]

    #Criando instâncias de uma propriedade de texto
    button_text = StringProperty(possibilities[0][0])
    label_text = StringProperty(possibilities[0][1])
    
    def on_click(self):
        self.possibilities = self.possibilities[::-1]
        
        self.button_text = self.possibilities[0][0]
        self.label_text = self.possibilities[0][1]

class MyFirstApp(App):
    pass

if __name__ == '__main__':
    MyFirstApp().run()
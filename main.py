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
    cont_aux = 1

    unidades = StringProperty(str(count))

    def soma_unidade(self):
        self.count += self.cont_aux
        self.unidades = str(self.count)
    
    def subtrai_unidade(self):
        self.count -= self.cont_aux
        self.unidades = str(self.count)
    
    def liga_desliga(self, botao_toggle):
        if botao_toggle.state == "normal":
            botao_toggle.text = "Off"
            self.cont_aux = 0

        elif botao_toggle.state == "down":
            botao_toggle.text = "On"
            self.cont_aux = 1

class MyFirstApp(App):
    pass

if __name__ == '__main__':
    MyFirstApp().run()

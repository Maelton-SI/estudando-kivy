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
from kivy.properties import BooleanProperty

class MainInterface(GridLayout):
    count = 0
    soma_button_disabled = BooleanProperty(True)
    sub_button_disabled = BooleanProperty(True)

    unidades = StringProperty(str(count))
    status_botao = StringProperty("Off")
    
    texto_instrutivo = StringProperty("Ligue a calculadora para poder calcular!")
    texto_explicativo = StringProperty()

    def soma_unidade(self):
        if not self.soma_button_disabled:
            self.count += 1
            self.unidades = str(self.count)
        
        if self.count == 10:
            self.soma_button_disabled = True
            self.texto_explicativo = "Esta calculadora não admite números maiores que 10 unidades."
        else:
            self.sub_button_disabled = False
            self.texto_explicativo = ""
    
    def subtrai_unidade(self):
        if not self.sub_button_disabled:
            self.count -= 1
            self.unidades = str(self.count)

        if self.count == 0:
            self.sub_button_disabled = True
            self.texto_explicativo = "Esta calculadora não admite números negativos."

        else:
            self.soma_button_disabled = False
            self.texto_explicativo = ""
    
    def liga_desliga(self, botao_toggle):
        if botao_toggle.state == "normal":
            self.soma_button_disabled = True
            self.sub_button_disabled = True

            self.count = 0
            self.unidades = str(self.count)
            
            self.status_botao = "Off"
            self.texto_instrutivo = "Ligue a calculadora para poder calcular!"
            self.texto_explicativo = ""

        elif botao_toggle.state == "down":
            self.soma_button_disabled = False
            
            self.status_botao = "On"
            self.texto_instrutivo = "Calculadora somatória ligada!"
            self.texto_explicativo = "Esta calculadora não admite números negativos."

class MyFirstApp(App):
    pass

if __name__ == '__main__':
    MyFirstApp().run()

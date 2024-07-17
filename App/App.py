import kivy
import kivy.app
import kivy.uix.label

class App(kivy.app.App):
    #Nuestra clase tiene que extenderse desde la clase de la aplicación
    def build(self):
        return kivy.uix.label.Label(text = "Simple App :D")
    
App().run()

if __name__== "__main__":
    App().run()
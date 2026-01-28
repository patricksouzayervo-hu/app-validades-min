from kivy.app import App
from kivy.uix.label import Label

class ValidadesApp(App):
    def build(self):
        return Label(text='APK OK')

if __name__ == '__main__':
    ValidadesApp().run()

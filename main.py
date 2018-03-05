from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class Andrzej(BoxLayout):
    pass

class MetUI(Widget):
    pass


class MetApp(App):
    def build(self):
        return MetUI(Andrzej)



if __name__ == '__main__':
    MetApp().run()
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.garden.matplotlib.backend_kivy import FigureCanvasKivy
import random
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color
import numpy as np






class PlotClass(BoxLayout):
    plt.plot([1, 23, 2, 4])
    plt.ylabel('some numbers')
    self.add_widget(FigureCanvasKivy(plt.gcf()))

class MetUI(BoxLayout):
    pass


class MetApp(App):
    def build(self):
        return MetUI()



if __name__ == '__main__':
    MetApp().run()

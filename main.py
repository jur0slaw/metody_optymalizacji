import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.garden.matplotlib.backend_kivy import FigureCanvasKivy
import random
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color,Rectangle
import numpy as np
from PSOAlgorithm import PSOAlgorithm

some_data = [1,2,3]

   

class PlotClass(FloatLayout):
    def DrawDifferent(self):
        for i in range(0,len(some_data)):
            some_data[i]+=1
        print(some_data)
        plt.plot(some_data, some_data, 'go-', label='line 1', linewidth=50)
        
        
    plt.plot(some_data, some_data, 'go-', label='line 1', linewidth=2)
    def __init__(self, **kwargs): 
        super(PlotClass, self).__init__(**kwargs)
        #plt.show()
        self.add_widget(FigureCanvasKivy(plt.gcf()))

class MetUI(BoxLayout):
    pass


class MetApp(App):
    def build(self):
        return MetUI()



if __name__ == '__main__':
    #PSO = PSOAlgorithm([-5, 5, -5, 5, 1001, 100, 0.7, 1.4])
    #PSO.start()
    MetApp().run()
    

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

from kivy.uix.widget import Widget

Builder.load_file('gui.kv')

class Main(Widget):
    def controlTheProgress(self, *args):
        value = args[1]
        
        # control angle end value via progress attribute
        self.ids.circular_progress.progress = value
        # control text progress value
        self.ids.circular_progress.text = f'{int(value/3.6)}%'
        
class MyApp(App):
    def build(self):
        return Main()

if __name__ == '__main__':
    MyApp().run()

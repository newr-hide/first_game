from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from random import randint

Window.clearcolor = (200 / 255, 215 / 255, 111 / 255, 1)
Window.title = "УГАДАЙКА"


class My_App(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Угадайка', color=(0,0,255)

        )


    def btn_pressed(self, *args):
        self.label.text = str(randint(1, 10))


    def build(self):
        box = BoxLayout()
        btn = Button(text="Угадай число и жми!",
                     color=(0,0,255),
                     background_normal='normal.png',
                     background_down='down.png',
                     border=(30, 30, 30, 30),
                     size_hint=(.3, .3),
                     pos_hint={"x": 0.35, "y": 0.3}
                     )
        btn.bind(on_press=self.btn_pressed)
        box.add_widget(self.label)
        box.add_widget(btn)

        return box
#213121

if __name__ == "__main__":
    My_App().run()

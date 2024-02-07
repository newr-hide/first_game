from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'resizable', True)

class ButtonApp(App):

    def build(self):
        btn = Button(text="Push Me !",
                     background_normal='images.normal3.png',
                     background_down='down2.png',
                     border=(30, 30, 30, 30),
                     size_hint=(.3, .3),
                     pos_hint={"x": 0.35, "y": 0.3}
                     )
        return btn

root = ButtonApp()
root.run()

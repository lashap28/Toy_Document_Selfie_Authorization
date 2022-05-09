import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


class SecondWidget(RelativeLayout):
    pass

class MainWidget(RelativeLayout):
    menu_widget = ObjectProperty()
    counter = 0

    def __init__(self,**kwargs):
        super(MainWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        self.counter += 1
        if self.counter > 130:
            self.menu_widget.opacity /= 1.006
        if self.counter > 180:
            self.menu_widget.opacity = 0


class testApp(App):
    pass


if __name__ == '__main__':
    testApp().run()

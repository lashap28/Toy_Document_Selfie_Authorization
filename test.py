from datetime import time
import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition



class AndroidCamera(RelativeLayout):
    pass

class ScreenOne(Screen):
    pass


class ScreenTwo(Screen):
    pass


class ScreenThree(Screen):
    pass


class AllScreenManager(ScreenManager):
    pass


class SecondWidget(RelativeLayout):
    pass


class MainWidget(RelativeLayout):
    menu_widget = ObjectProperty()
    counter = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / 60)

    def update(self, dt):
        self.counter += 1
        if self.counter > 90:
            self.menu_widget.opacity /= 1.009
        if self.counter > 180:
            self.menu_widget.opacity = 0


class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

kv = Builder.load_file("testscreen.kv")

class TestScreenApp(App):
    def build(self):
        return kv


TestScreenApp().run()

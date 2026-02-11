from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.animation import Animation

try:
    from jnius import autoclass
    Build = autoclass("android.os.Build")
    VERSION = autoclass("android.os.Build$VERSION")
    DEVICE_MODEL = Build.MODEL
    ANDROID_VER = VERSION.RELEASE
except:
    DEVICE_MODEL = "Unknown Device"
    ANDROID_VER = "Unknown"


class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        with layout.canvas.before:
            Color(1,1,1,1)
            Rectangle(size=Window.size,pos=(0,0))

        btn=Button(text="START",size_hint=(0.35,0.15),
                   pos_hint={"center_x":0.5,"center_y":0.5},
                   font_size=40,background_color=(0,0,0,1),color=(1,1,1,1))
        btn.bind(on_release=lambda x:setattr(self.manager,"current","loading"))
        layout.add_widget(btn)
        self.add_widget(layout)


class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout=FloatLayout()
        with self.layout.canvas.before:
            Color(1,1,1,1)
            Rectangle(size=Window.size,pos=(0,0))

        self.label=Label(text="Checking Device...",
                         pos_hint={"center_x":0.5,"center_y":0.65},
                         font_size=30,color=(0,0,0,1))
        self.bar=ProgressBar(max=100,value=0,
                             size_hint=(0.7,0.05),
                             pos_hint={"center_x":0.5,"center_y":0.5})
        self.percent=Label(text="0%",
                           pos_hint={"center_x":0.5,"center_y":0.42},
                           font_size=25,color=(0,0,0,1))
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.bar)
        self.layout.add_widget(self.percent)
        self.add_widget(self.layout)

    def on_enter(self):
        self.ev=Clock.schedule_interval(self.update,0.04)

    def update(self,dt):
        self.bar.value+=1
        self.percent.text=f"{int(self.bar.value)}%"
        if self.bar.value>=100:
            Clock.unschedule(self.ev)
            self.manager.current="error"


class ErrorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout=FloatLayout()
        with self.layout.canvas.before:
            Color(1,1,1,1)
            Rectangle(size=Window.size,pos=(0,0))

        self.info=Label(text=f"""Device Model : {DEVICE_MODEL}
Android Version : {ANDROID_VER}
Security Patch : Supported

Your Device Version Not Support:""",
                        font_size=28,halign="center",valign="middle",color=(0,0,0,1))
        self.info.bind(size=self.info.setter("text_size"))
        self.layout.add_widget(self.info)
        self.add_widget(self.layout)

    def on_enter(self):
        Clock.schedule_once(self.crash,3)

    def crash(self,dt):
        anim=Animation(x=10,duration=0.05)+Animation(x=-10,duration=0.05)
        anim.repeat=6
        anim.start(self.layout)
        self.popup()

    def popup(self):
        box=BoxLayout(orientation="vertical",padding=15,spacing=10)
        msg=Label(text="App isn't responding.",font_size=22)

        btns=BoxLayout(size_hint_y=None,height=50,spacing=10)
        close_btn=Button(text="Close App")
        wait_btn=Button(text="Wait")
        update_btn=Button(text="Update App")

        btns.add_widget(close_btn)
        btns.add_widget(wait_btn)
        btns.add_widget(update_btn)

        box.add_widget(msg)
        box.add_widget(btns)

        pop=Popup(title="System",content=box,size_hint=(0.85,0.35),auto_dismiss=False)
        wait_btn.bind(on_release=pop.dismiss)
        close_btn.bind(on_release=App.get_running_app().stop)
        update_btn.bind(on_release=lambda x:self.fake_update())
        pop.open()

    def fake_update(self):
        self.layout.clear_widgets()
        label=Label(text="Downloading Update...",
                    pos_hint={"center_x":0.5,"center_y":0.65},
                    font_size=30,color=(0,0,0,1))
        self.bar=ProgressBar(max=100,value=0,
                             size_hint=(0.7,0.05),
                             pos_hint={"center_x":0.5,"center_y":0.5})
        self.percent=Label(text="0%",
                           pos_hint={"center_x":0.5,"center_y":0.42},
                           font_size=25,color=(0,0,0,1))
        self.layout.add_widget(label)
        self.layout.add_widget(self.bar)
        self.layout.add_widget(self.percent)
        Clock.schedule_interval(self.loop,0.05)

    def loop(self,dt):
        self.bar.value+=1
        if self.bar.value>=99:
            self.bar.value=82
        self.percent.text=f"{int(self.bar.value)}%"


class MyApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(StartScreen(name="start"))
        sm.add_widget(LoadingScreen(name="loading"))
        sm.add_widget(ErrorScreen(name="error"))
        Window.bind(on_keyboard=self.disable_back)
        return sm

    def disable_back(self,window,key,*largs):
        if key==27:
            return True


MyApp().run()
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import kivy
from App import DbCon
from kivy.core.window import Window

Window.clearcolor = kivy.utils.get_color_from_hex('#808080')

class Home(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText
        self.db = DbCon.DbCon()
        if self.db.get_user_ac(app.username,app.password) :

            print(app.username)
            print(app.password)

            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'
        else:
            print("Wrong")


    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Home(name='connected'))

        return manager

if __name__ == '__main__':
    LoginApp().run()

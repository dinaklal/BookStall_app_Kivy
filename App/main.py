from kivy.app import App
from kivy.properties import StringProperty,OptionProperty,ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.tabbedpanel import TabbedPanel
import kivy
from App import DbCon
from kivy.core.window import Window
from App import home
from kivy.lang import Builder
Builder.load_file('login.kv')
Builder.load_file('AddItem.kv')
Window.clearcolor = kivy.utils.get_color_from_hex('#808080')



class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        self.db = DbCon.DbCon()
        res = self.db.get_gst()
        app.gst={}
        for row in res:
            print (row[0])
            app.gst.append(row[0])

        if self.db.get_user_ac(app.username,app.password) :

            print(app.username)
            print(app.password)

            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'
        else:
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'error'


    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)
    gst =  ListProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(home.Home(name='connected'))
        manager.add_widget(home.LoginError(name='error'))
        manager.add_widget(home.AddItem(name="AddItem"))

        return manager

if __name__ == '__main__':
    LoginApp().run()

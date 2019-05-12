from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.app import App
from App import DbCon
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

class Home(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
class LoginError(Screen):
    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
class AddItem(Screen):


    def submit_details(self,item,price,qtty,gst,cat):
        app = App.get_running_app()
        print(app.username + " "+ item+"  "+ " "+ price+" "+ qtty+" "+gst)
        self.db = DbCon.DbCon()
        res= self.db.add_item(item,price,qtty,gst,cat,app.userid)

        show_pop()
        self.resetForm()
    def resetForm(self):
        self.ids['item'].text = ""
        self.ids['price'].text = ""
        self.ids['qtty'].text = ""
        self.ids['gst'].text = "GST Class"
        self.ids['category'].text = "Category"


class pop_Up(FloatLayout):
    tex="Item Added Successfully"
    pass

def show_pop():
    #print()
    show = pop_Up()

    popUp_window = Popup(title="Popup Window",content=show,size_hint=(None,None),size=(400,400),auto_dismiss=False)
    show.ids.button.bind(on_press=popUp_window.dismiss)
    popUp_window.open()


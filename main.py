from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import BooleanProperty,ObjectProperty
#from newtabs import TabbedPanelContent,TabbedPanelException,TabbedPanelItem,TabbedPanelStrip,TabbedPanelHeader,TabbedPanel


class Tab1(BoxLayout):
    
    def Expanded_tab(self,instance):
        instance.parent.parent.parent.parent.ids.ibl.is_expanded = False

class Tab2(BoxLayout):
    pass

class Tab3(BoxLayout):
    pass

class Ctabs(BoxLayout):
    pass

class IconBarLeft(BoxLayout):
    
    is_expanded = BooleanProperty(False)
    ibl = ObjectProperty()
    icon1 = ObjectProperty()
    icon2 = ObjectProperty()
    icon3 = ObjectProperty()
    
    tab1 = ObjectProperty()
    
    def __init__(self,**kwargs):
        super(IconBarLeft,self).__init__(**kwargs)

        
    def Add_Tab1(self):
        if self.is_expanded == False:
            self.parent.ids.ct.add_widget(Tab1())
        self.is_expanded = True

class Icons(ButtonBehavior,Image):
    is_expanded = BooleanProperty(False)
    tab = ObjectProperty()
    
    def __init__(self,**kwargs):
        super(Icons,self).__init__(**kwargs)

class Container(BoxLayout):
    ct = ObjectProperty()
    ctabs = ObjectProperty()
    iconBarRight = ObjectProperty()
    iconBarLeft = ObjectProperty()
    
    def __init__(self,**kwargs):
        super(Container,self).__init__(**kwargs)

class MainApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    app = MainApp()
    app.run()
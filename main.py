import kivy


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel

from kivy.lang import Builder
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

import sys
sys.path.insert(0,'/home/coy/.virtualenvs/mlog/share/kivy-examples/widgets/recycleview')
sys.path.insert(0,'/home/coy/Devel/testfolders') 
from basic_data import Test,TestApp
from rv import RV

class MineLog(BoxLayout):
    pass
        
class EquipmentBoxLayout(BoxLayout):
    pass
class EquipmentDataView(GridLayout):
    pass
class EquipmentPanel(TabbedPanel):
    pass
class MineLogApp(App):
    def build(self):
        self.root = Builder.load_file('gui_mlog.kv')

if __name__ == '__main__':
    MineLogApp().run()


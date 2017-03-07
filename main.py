import MineLog as mlog
from multiprocessing import Process


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
    
    y1=mlog.mload('Equipment1.mlog')
    y2=mlog.mload('Equipment2.mlog')
    y3=mlog.mload('Equipment3.mlog')

    eq_list=[y1,y2,y3]
    eq_rv=ObjectProperty(None)

    eq_rv_list = [{'text': x.Name,'value':x } for x in eq_list] 
    shiftrv_data = [{'text': "Truck"+str(x),'value':x} for x in range(20)] 
    def eq_plot(self):
        for i in self.eq_rv.data_model.__dict__:print(i)
        # temp=self.eq_rv.data_model.last_len
        temp=self.eq_rv.view_adapter.views
        for i in temp:
            if temp[i].selected:
                ind=temp[i].index
                proc=Process(target=mlog.oeeEquipmentPlot,args=(self.eq_rv_list[ind]['value'],))
                proc.start()
    def new_eq(self):
        pass


    
class EquipmentPanel(TabbedPanel):
    pass
class MineLogApp(App):
    def build(self):
        self.root = Builder.load_file('gui_mlog.kv')

if __name__ == '__main__':
    MineLogApp().run()


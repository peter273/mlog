# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Mar 19 18:46:29 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui

#Mine Log 
# import MineLog as ml
from MineLog import Equipment,ShiftFile,mload,oeeEquipmentPlot,Moving_AveragePlot 

import os


#New Equipment Dialog
from mlogUI.neweqdialog import Ui_Dialog
class NewEqDialog(QtGui.QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
    def getValues(self):
        name=self.eqName_lineedit.text()
        eqtype= self.eqtype_combobox.currentText()
        return (str(name).strip(),str(eqtype))

from mlogUI import mwindow
class MainUI(mwindow.Ui_MainWindow):
    def setupUi(self,MainWindow):
        super(MainUI,self).setupUi(MainWindow)
        self.ext_init()
    def ext_init(self):
        self.plot_toolbtn.clicked.connect(self.plt_btn_clicked)
        self.shovel_listwidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.truck_listwidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.shovel_listwidget.currentItemChanged.connect(self.item_click)
        self.ma_checkbox.stateChanged.connect(self.maspinner_changestate)
        self.ma_spinBox.setEnabled(False)
        self.get_initial_equipment_list()

        # for i in range(1,21):
        #     name = "Shovel{0}".format(i)
        #     shovel_item=QtGui.QListWidgetItem()
        #     shovel_item.setText(name)
        #     self.shovel_listwidget.addItem(shovel_item)
        #     cut_data=Data(i)
        #     shovel_item.setData(QtCore.Qt.UserRole,cut_data)
        # for i in range(1,21):
        #     self.truck_listwidget.addItem("Truck{0}".format(i))
    # Change Spinner state when Moving Average check box state changes
    def maspinner_changestate(self):
        if self.ma_checkbox.isChecked():
            self.ma_spinBox.setEnabled(True)
        else:
            self.ma_spinBox.setEnabled(False)
    def item_click(self,arg=None):
        #TODO change data to view upon change equipment
        pass

    # Return the Time Frame to be Plotted
    def chosen_dataframe(self):
        x={'shiftly':self.shift_rb,
            'daily':self.day_rb,
            'weekly':self.week_rb,
            'monthly':self.month_rb}
        for i in x:
            if x[i].isChecked():
                return i
    # Return a list of Chosen Equipment
    def chosen_equipment(self):
        #0-shovels,1-trucks
        eqlist=self.eq_tab.currentIndex()
        if eqlist==0: eq_listwidget=self.shovel_listwidget
        elif eqlist==1: eq_listwidget=self.truck_listwidget

        x = eq_listwidget.selectedItems()
        return x
    # Returns a list of chosen parameters
    def chosen_params(self):
        params=[]
        cbox=[self.availability_checkbox,
                self.utilization_checkbox,
                self.eff_checkbox,
                self.oee_checkbox]
        for i in cbox:
            if i.checkState():
                params.append(i.text())
        return params

    def plt_btn_clicked(self):
        eq = self.chosen_equipment()
        eqpment = [i.data(QtCore.Qt.UserRole) for i in eq]
        data_frame=self.chosen_dataframe()
        params=self.chosen_params()

        moving_ave_on=self.ma_checkbox.checkState()
        interval = (self.ma_spinBox.value())
        if eqpment and params and not moving_ave_on:
            oeeEquipmentPlot(eqpment,params,data_frame)
        if moving_ave_on and eqpment and params:
            Moving_AveragePlot(eqpment,params,data_frame,interval=interval)
        # TODO add dialog for no chosen parameter/equipment


    def get_initial_equipment_list(self):
        dirpath=os.path.dirname(__file__)
        filepath = os.path.join(dirpath,'Equipment')
        eq_filenames = [i for i in os.listdir(filepath) if i.endswith(".mlog")]
        eq_list=[]

        listwidget=self.shovel_listwidget
        for i in eq_filenames:
            eq=mload(os.path.join(filepath,i))

            if eq.Type=="Shovel": 
                listwidget=self.shovel_listwidget
            else:
                listwidget=self.truck_listwidget

            eq_item=QtGui.QListWidgetItem()
            eq_item.setText(eq.Name)
            eq_item.setData(QtCore.Qt.UserRole,eq)

            listwidget.addItem(eq_item)
            listwidget.repaint()

class MineLog(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MineLog,self).__init__(parent)
        # self.ui=Ui_MainWindow()
        self.ui=MainUI()
        self.ui.setupUi(self)
        self.ui.new_toolbtn.clicked.connect(self.new_buttonClicked)
        self.ui.addshift_toolbtn.clicked.connect(self.func_addshift)
        self.ui.delete_toolbtn.clicked.connect(self.func_deleq)
        #TODO check if Equipment folder exists

    def func_deleq(self):
        x=self.ui.chosen_equipment()
        if len(x)>0:
            msg = "Are you sure you want to delete chosen Equipment?"
            reply =QtGui.QMessageBox.question(self,'Message',msg,QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.delete_equipment()
        else:
            msg = QtGui.QMessageBox(self)
            msg.setText('No Chosen Equipment')
            msg.setWindowTitle("Warning")
            msg.show()

    def func_addshift(self):
        # TODO add shift option to add from folder
        dirpath=os.path.dirname(__file__)
        filepath = os.path.join(dirpath,'Equipment')
        eq=self.ui.chosen_equipment()
        if len(eq)==1:
            fname,fx = QtGui.QFileDialog.getOpenFileNames()
            g=eq[0].data(QtCore.Qt.UserRole)
            notadded=[]
            for sfile in fname:
                if g.AddFile(sfile): print('{0} is added'.format(sfile))
                else:
                    notadded.append(os.path.basename(sfile))
                    print("Error in Adding {0}".format(sfile))
            if notadded:
                msg = "Error in Adding {0} out of {1} file/s:\n".format(len(notadded),len(fname))
                msg += "Do you wish to continue adding files that can be Added?"
                reply = QtGui.QMessageBox.question(self,'Message',msg,QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    g.update()
                    g.save(filepath)
            else:
                g.update()
                g.save(filepath)
        else:
            msg = QtGui.QMessageBox(self)
            msg.setText('Choose only one Equipment')
            msg.setWindowTitle("Warning")
            msg.show()

    def new_buttonClicked(self):
        dialog = NewEqDialog(self)
        if dialog.exec_():
            eq_name,eq_type=dialog.getValues()
            if eq_name=="":
                msg = QtGui.QMessageBox(dialog)
                msg.setText('Equipment name cannot be empty')
                msg.setWindowTitle("Warning")
                msg.show()
            else: 
                self.create_equipment(eq_name,eq_type)
    def delete_equipment(self):
        dirpath=os.path.dirname(__file__)
        filepath = os.path.join(dirpath,'Equipment')
        if not os.path.exists(filepath):
            os.mkdir(filepath)

        eqlist=self.ui.eq_tab.currentIndex()
        if eqlist==0: eq_listwidget=self.ui.shovel_listwidget
        elif eqlist==1: eq_listwidget=self.ui.truck_listwidget
        
        x = eq_listwidget.selectedItems()
        for i in x:
            eq_listwidget.takeItem(eq_listwidget.row(i))
            g = i.data(QtCore.Qt.UserRole)
            os.remove(os.path.join(filepath,g.Name+".mlog"))

    def create_equipment(self,name,eq_type):
        #TODO Check if Equipment Name Already exist
        import os
        dirpath= os.path.dirname(__file__)
        filepath= os.path.join(dirpath,'Equipment')
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        new_eq=Equipment(name)
        new_eq.save(filepath)

        eq_item=QtGui.QListWidgetItem()
        eq_item.setText(name)
        eq_item.setData(QtCore.Qt.UserRole,new_eq)

        if eq_type=="Shovel": listwidget=self.ui.shovel_listwidget
        elif eq_type=="Truck": listwidget=self.ui.truck_listwidget

        listwidget.addItem(eq_item)
        listwidget.repaint()

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    win =MineLog()
    win.show()
    sys.exit(app.exec_())

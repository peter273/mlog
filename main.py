# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Mar 19 18:46:29 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui


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

class Data:
    def __init__(self,val):
        self.val=val
    def getval(self):
        return self.val

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

        for i in range(1,21):
            name = "Shovel{0}".format(i)
            shovel_item=QtGui.QListWidgetItem()
            shovel_item.setText(name)
            self.shovel_listwidget.addItem(shovel_item)
            cut_data=Data(i)
            shovel_item.setData(QtCore.Qt.UserRole,cut_data)
        for i in range(1,21):
            self.truck_listwidget.addItem("Truck{0}".format(i))
    # Change Spinner state when Moving Average check box state changes
    def maspinner_changestate(self):
        if self.ma_checkbox.isChecked():
            self.ma_spinBox.setEnabled(True)
        else:
            self.ma_spinBox.setEnabled(False)
    def item_click(self,arg=None):
        cut_data = arg.data(QtCore.Qt.UserRole)
        print("item click ",cut_data.getval())

    # Return the Time Frame to be Plotted
    def chosen_dataframe(self):
        x=[self.shift_rb,
            self.day_rb,
            self.week_rb,
            self.month_rb]
        for i in x:
            if i.isChecked():
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
        eq=self.chosen_equipment()
        data_fram=self.chosen_dataframe()
        params=self.chosen_params()

        print(list(map(lambda s: s.text(), eq)))
        print(self.chosen_dataframe().text())
        print(params)

class MineLog(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MineLog,self).__init__(parent)
        # self.ui=Ui_MainWindow()
        self.ui=MainUI()
        self.ui.setupUi(self)
        self.ui.new_toolbtn.clicked.connect(self.new_buttonClicked)
        self.ui.addshift_toolbtn.clicked.connect(self.func_addshift)
        self.ui.delete_toolbtn.clicked.connect(self.func_deleq)

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
        eq=self.ui.chosen_equipment()
        if len(eq)==1:
            fname = QtGui.QFileDialog.getOpenFileNames()
            # TODO add shift function
            print(fname)
        else:
            msg = QtGui.QMessageBox(self)
            msg.setText('Choose only one Equipment')
            msg.setWindowTitle("Warning")
            msg.show()

    def new_buttonClicked(self):
        dialog = NewEqDialog(self)
        if dialog.exec_():
            eq_name,eq_type=dialog.getValues()
            # TODO new equipment function
            if eq_name=="":
                msg = QtGui.QMessageBox(dialog)
                msg.setText('Equipment name cannot be empty')
                msg.setWindowTitle("Warning")
                msg.show()
            else: 
                self.create_equipment(eq_name)
    def delete_equipment(self):
        eqlist=self.ui.eq_tab.currentIndex()
        if eqlist==0: eq_listwidget=self.ui.shovel_listwidget
        elif eqlist==1: eq_listwidget=self.ui.truck_listwidget
        
        x = eq_listwidget.selectedItems()
        for i in x:
            eq_listwidget.takeItem(eq_listwidget.row(i))
    def create_equipment(self,name):
        import os
        cwd=os.getcwd()
        # filepath= os.path.join(cwd,'Equipment')
        new_eq=Data(name)

        shovel_item=QtGui.QListWidgetItem()
        shovel_item.setText(name)
        data=Data(name)
        self.ui.shovel_listwidget.addItem(shovel_item)
        self.ui.shovel_listwidget.repaint()
        shovel_item.setData(QtCore.Qt.UserRole,data)

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    win =MineLog()
    win.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui

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
class EqItemGui:
    def __init__(self,eq,eq_gui):
        self.eq=eq
        self.eq_gui

from mlogUI import mwindow
class MainUI(mwindow.Ui_MainWindow):
    def setupUi(self,MainWindow):
        super(MainUI,self).setupUi(MainWindow)
        dirname=os.path.dirname(__file__)

        icon_path={
                'new':['plus.png',self.new_toolbtn],
                'delete':['cancel-2.png',self.delete_toolbtn],
                'addshift':['copy.png',self.addshift_toolbtn],
                'info':['information.png',self.info_toolbtn],
                'plot':['next-1.png',self.plot_toolbtn]}

        for i in icon_path:
            icon_path[i][0]=os.path.join(dirname,"mlogUI/flaticons/icons/png/"+icon_path[i][0])
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path[i][0]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            icon_path[i][1].setIcon(icon)
            icon_path[i][1].setIconSize(QtCore.QSize(30, 30))

        self.plot_toolbtn.clicked.connect(self.plt_btn_clicked)
        self.shovel_listwidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.shovel_listwidget.itemSelectionChanged.connect(self.itemSelectionChanged)
        self.truck_listwidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ma_checkbox.stateChanged.connect(self.maspinner_changestate)
        self.ma_spinBox.setEnabled(False)
        self.get_initial_equipment_list()

        self.display_headers()
        self.data_to_display=[]
    # Display Headers
    def display_headers(self):
        header=QtGui.QTreeWidgetItem([
            "Name",
            "OEE",
            "Availability",
            "Utilization",
            "Efficiency"])
        self.data_listwidget.setHeaderItem(header)

    # Change Moving Average Spinner state when Moving Average check box state changes
    def maspinner_changestate(self):
        if self.ma_checkbox.isChecked():
            self.ma_spinBox.setEnabled(True)
        else:
            self.ma_spinBox.setEnabled(False)

    def itemSelectionChanged(self):
        #TODO change data to view upon change equipment
        
        eq = self.chosen_equipment()
        eqpment = [i.data(QtCore.Qt.UserRole) for i in eq]
        data_frame=self.chosen_dataframe()

        # eqlist=self.eq_tab.currentIndex()
        # if eqlist==0: eq_listwidget=self.shovel_listwidget
        # elif eqlist==1: eq_listwidget=self.truck_listwidget

        # eqpment= [i.data(
        # for i in range(eq_listwidget.count()): 
        #     print(eq_listwidget.item(i))

        header=QtGui.QTreeWidgetItem([
            "Name",
            "OEE",
            "Availability",
            "Utilization",
            "Efficiency"])
        main_=self.data_listwidget
        main_.clear()
        main_.setHeaderItem(header)
        for i in eqpment:
            eq_item=QtGui.QTreeWidgetItem(main_,[i.Name])
            eq_item.setData(2,QtCore.Qt.UserRole,i)
            attributes=["OEE",
                    "Availability",
                    "Utilization",
                    "Efficiency"]
            for ctr in range(len(i.Data)):
                Date=str(i.Data.iloc[ctr].Date.date())
                Shift=i.Data.iloc[ctr].Shift
                param=[str(getattr(i.Data.iloc[ctr],temp)) for temp in attributes]
                shift_item=QtGui.QTreeWidgetItem(eq_item,[Date+" Shift "+Shift,
                    *param])
                    

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
    # Plotting of Data 
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

    # Delete Equipment Function
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

    # Add Shift Function
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
    # Opens Dialog for Creating New Equipment
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
    # Function for creating New Equipment
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Mar 19 18:46:29 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.new_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.new_toolbtn.setObjectName("new_toolbtn")
        self.horizontalLayout_8.addWidget(self.new_toolbtn)
        self.delete_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.delete_toolbtn.setObjectName("delete_toolbtn")
        self.horizontalLayout_8.addWidget(self.delete_toolbtn)
        self.addshift_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.addshift_toolbtn.setObjectName("addshift_toolbtn")
        self.horizontalLayout_8.addWidget(self.addshift_toolbtn)
        self.plot_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.plot_toolbtn.setObjectName("plot_toolbtn")
        self.horizontalLayout_8.addWidget(self.plot_toolbtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.eq_tab = QtGui.QTabWidget(self.splitter)
        self.eq_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eq_tab.setObjectName("eq_tab")
        self.shovel_tab = QtGui.QWidget()
        self.shovel_tab.setObjectName("shovel_tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.shovel_tab)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shovel_listwidget = QtGui.QListWidget(self.shovel_tab)
        self.shovel_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.shovel_listwidget.setFrameShadow(QtGui.QFrame.Plain)
        self.shovel_listwidget.setObjectName("shovel_listwidget")
        self.verticalLayout.addWidget(self.shovel_listwidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.eq_tab.addTab(self.shovel_tab, "")
        self.truck_tab = QtGui.QWidget()
        self.truck_tab.setObjectName("truck_tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.truck_tab)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.truck_listwidget = QtGui.QListWidget(self.truck_tab)
        self.truck_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.truck_listwidget.setObjectName("truck_listwidget")
        self.verticalLayout_2.addWidget(self.truck_listwidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.eq_tab.addTab(self.truck_tab, "")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.availability_checkbox = QtGui.QCheckBox(self.groupBox)
        self.availability_checkbox.setObjectName("availability_checkbox")
        self.verticalLayout_5.addWidget(self.availability_checkbox)
        self.utilization_checkbox = QtGui.QCheckBox(self.groupBox)
        self.utilization_checkbox.setObjectName("utilization_checkbox")
        self.verticalLayout_5.addWidget(self.utilization_checkbox)
        self.eff_checkbox = QtGui.QCheckBox(self.groupBox)
        self.eff_checkbox.setObjectName("eff_checkbox")
        self.verticalLayout_5.addWidget(self.eff_checkbox)
        self.oee_checkbox = QtGui.QCheckBox(self.groupBox)
        self.oee_checkbox.setChecked(True)
        self.oee_checkbox.setObjectName("oee_checkbox")
        self.verticalLayout_5.addWidget(self.oee_checkbox)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.shift_rb = QtGui.QRadioButton(self.groupBox_2)
        self.shift_rb.setChecked(True)
        self.shift_rb.setObjectName("shift_rb")
        self.verticalLayout_8.addWidget(self.shift_rb)
        self.day_rb = QtGui.QRadioButton(self.groupBox_2)
        self.day_rb.setObjectName("day_rb")
        self.verticalLayout_8.addWidget(self.day_rb)
        self.week_rb = QtGui.QRadioButton(self.groupBox_2)
        self.week_rb.setObjectName("week_rb")
        self.verticalLayout_8.addWidget(self.week_rb)
        self.month_rb = QtGui.QRadioButton(self.groupBox_2)
        self.month_rb.setObjectName("month_rb")
        self.verticalLayout_8.addWidget(self.month_rb)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ma_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.ma_spinBox.setObjectName("ma_spinBox")
        self.horizontalLayout_7.addWidget(self.ma_spinBox)
        self.ma_checkbox = QtGui.QCheckBox(self.layoutWidget)
        self.ma_checkbox.setObjectName("ma_checkbox")
        self.horizontalLayout_7.addWidget(self.ma_checkbox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.info_listwidget = QtGui.QTabWidget(self.splitter_2)
        self.info_listwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info_listwidget.setObjectName("info_listwidget")
        self.information_tab = QtGui.QWidget()
        self.information_tab.setObjectName("information_tab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.information_tab)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget_3 = QtGui.QListWidget(self.information_tab)
        self.listWidget_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget_3.setFrameShadow(QtGui.QFrame.Plain)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_3.addWidget(self.listWidget_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.info_listwidget.addTab(self.information_tab, "")
        self.data_tab = QtGui.QWidget()
        self.data_tab.setObjectName("data_tab")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.data_tab)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.data_listwidget = QtGui.QListWidget(self.data_tab)
        self.data_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.data_listwidget.setObjectName("data_listwidget")
        self.verticalLayout_4.addWidget(self.data_listwidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.info_listwidget.addTab(self.data_tab, "")
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionAdd_Shift = QtGui.QAction(MainWindow)
        self.actionAdd_Shift.setObjectName("actionAdd_Shift")

        self.retranslateUi(MainWindow)
        self.eq_tab.setCurrentIndex(0)
        self.info_listwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ext_init()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MineLog", None, QtGui.QApplication.UnicodeUTF8))
        self.new_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.addshift_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "Add Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.plot_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.eq_tab.setTabText(self.eq_tab.indexOf(self.shovel_tab), QtGui.QApplication.translate("MainWindow", "Shovel", None, QtGui.QApplication.UnicodeUTF8))
        self.eq_tab.setTabText(self.eq_tab.indexOf(self.truck_tab), QtGui.QApplication.translate("MainWindow", "Truck", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.availability_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Availability", None, QtGui.QApplication.UnicodeUTF8))
        self.utilization_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Utilization", None, QtGui.QApplication.UnicodeUTF8))
        self.eff_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Efficiency", None, QtGui.QApplication.UnicodeUTF8))
        self.oee_checkbox.setText(QtGui.QApplication.translate("MainWindow", "OEE", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Data Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.shift_rb.setText(QtGui.QApplication.translate("MainWindow", "Per Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.day_rb.setText(QtGui.QApplication.translate("MainWindow", "Per Day", None, QtGui.QApplication.UnicodeUTF8))
        self.week_rb.setText(QtGui.QApplication.translate("MainWindow", "Per Week", None, QtGui.QApplication.UnicodeUTF8))
        self.month_rb.setText(QtGui.QApplication.translate("MainWindow", "Per Month", None, QtGui.QApplication.UnicodeUTF8))
        self.ma_checkbox.setText(QtGui.QApplication.translate("MainWindow", "Moving Average", None, QtGui.QApplication.UnicodeUTF8))
        self.info_listwidget.setTabText(self.info_listwidget.indexOf(self.information_tab), QtGui.QApplication.translate("MainWindow", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.info_listwidget.setTabText(self.info_listwidget.indexOf(self.data_tab), QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Shift.setText(QtGui.QApplication.translate("MainWindow", "Add Shift", None, QtGui.QApplication.UnicodeUTF8))

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

#New Equipment Dialog
from neweqdialog import Ui_Dialog
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
    

class MineLog(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MineLog,self).__init__(parent)
        self.ui=Ui_MainWindow()
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

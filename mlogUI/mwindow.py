# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwindow.ui'
#
# Created: Wed Mar 22 02:00:07 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(547, 516)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.new_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.new_toolbtn.setMouseTracking(False)
        self.new_toolbtn.setToolTip("")
        self.new_toolbtn.setStatusTip("")
        self.new_toolbtn.setWhatsThis("")
        self.new_toolbtn.setIconSize(QtCore.QSize(30, 30))
        self.new_toolbtn.setShortcut("")
        self.new_toolbtn.setCheckable(False)
        self.new_toolbtn.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.new_toolbtn.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.new_toolbtn.setObjectName("new_toolbtn")
        self.horizontalLayout_6.addWidget(self.new_toolbtn)
        self.delete_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.delete_toolbtn.setIconSize(QtCore.QSize(30, 30))
        self.delete_toolbtn.setShortcut("")
        self.delete_toolbtn.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.delete_toolbtn.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.delete_toolbtn.setObjectName("delete_toolbtn")
        self.horizontalLayout_6.addWidget(self.delete_toolbtn)
        self.addshift_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.addshift_toolbtn.setIconSize(QtCore.QSize(30, 30))
        self.addshift_toolbtn.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.addshift_toolbtn.setObjectName("addshift_toolbtn")
        self.horizontalLayout_6.addWidget(self.addshift_toolbtn)
        self.info_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.info_toolbtn.setIconSize(QtCore.QSize(30, 30))
        self.info_toolbtn.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.info_toolbtn.setObjectName("info_toolbtn")
        self.horizontalLayout_6.addWidget(self.info_toolbtn)
        self.plot_toolbtn = QtGui.QToolButton(self.centralwidget)
        self.plot_toolbtn.setIconSize(QtCore.QSize(30, 30))
        self.plot_toolbtn.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.plot_toolbtn.setObjectName("plot_toolbtn")
        self.horizontalLayout_6.addWidget(self.plot_toolbtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setChildrenCollapsible(False)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.frame = QtGui.QFrame(self.splitter_2)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.calendarWidget = QtGui.QCalendarWidget(self.frame)
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_8.addWidget(self.calendarWidget)
        self.frame_2 = QtGui.QFrame(self.splitter_2)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtGui.QGroupBox(self.frame_2)
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
        self.groupBox_2 = QtGui.QGroupBox(self.frame_2)
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
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(15, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ma_spinBox = QtGui.QSpinBox(self.frame_2)
        self.ma_spinBox.setObjectName("ma_spinBox")
        self.horizontalLayout_7.addWidget(self.ma_spinBox)
        self.ma_checkbox = QtGui.QCheckBox(self.frame_2)
        self.ma_checkbox.setObjectName("ma_checkbox")
        self.horizontalLayout_7.addWidget(self.ma_checkbox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.splitter = QtGui.QSplitter(self.splitter_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.eq_tab = QtGui.QTabWidget(self.splitter)
        self.eq_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.eq_tab.setObjectName("eq_tab")
        self.shovel_tab = QtGui.QWidget()
        self.shovel_tab.setObjectName("shovel_tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.shovel_tab)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.shovel_listwidget = QtGui.QListWidget(self.shovel_tab)
        self.shovel_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.shovel_listwidget.setFrameShadow(QtGui.QFrame.Plain)
        self.shovel_listwidget.setObjectName("shovel_listwidget")
        self.horizontalLayout_2.addWidget(self.shovel_listwidget)
        self.eq_tab.addTab(self.shovel_tab, "")
        self.truck_tab = QtGui.QWidget()
        self.truck_tab.setObjectName("truck_tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.truck_tab)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.truck_listwidget = QtGui.QListWidget(self.truck_tab)
        self.truck_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.truck_listwidget.setObjectName("truck_listwidget")
        self.horizontalLayout.addWidget(self.truck_listwidget)
        self.eq_tab.addTab(self.truck_tab, "")
        self.info_listwidget = QtGui.QTabWidget(self.splitter)
        self.info_listwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info_listwidget.setObjectName("info_listwidget")
        self.data_tab = QtGui.QWidget()
        self.data_tab.setObjectName("data_tab")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.data_tab)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.data_listwidget = QtGui.QTreeWidget(self.data_tab)
        self.data_listwidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.data_listwidget.setObjectName("data_listwidget")
        self.data_listwidget.headerItem().setText(0, "1")
        self.horizontalLayout_4.addWidget(self.data_listwidget)
        self.info_listwidget.addTab(self.data_tab, "")
        self.information_tab = QtGui.QWidget()
        self.information_tab.setObjectName("information_tab")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.information_tab)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget_3 = QtGui.QTableWidget(self.information_tab)
        self.tableWidget_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget_3.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget_3)
        self.info_listwidget.addTab(self.information_tab, "")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 23))
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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MineLog", None, QtGui.QApplication.UnicodeUTF8))
        self.new_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "New File", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.addshift_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "Add Shift File", None, QtGui.QApplication.UnicodeUTF8))
        self.info_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.plot_toolbtn.setText(QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
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
        self.eq_tab.setTabText(self.eq_tab.indexOf(self.shovel_tab), QtGui.QApplication.translate("MainWindow", "Shovel", None, QtGui.QApplication.UnicodeUTF8))
        self.eq_tab.setTabText(self.eq_tab.indexOf(self.truck_tab), QtGui.QApplication.translate("MainWindow", "Truck", None, QtGui.QApplication.UnicodeUTF8))
        self.info_listwidget.setTabText(self.info_listwidget.indexOf(self.data_tab), QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.info_listwidget.setTabText(self.info_listwidget.indexOf(self.information_tab), QtGui.QApplication.translate("MainWindow", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Shift.setText(QtGui.QApplication.translate("MainWindow", "Add Shift", None, QtGui.QApplication.UnicodeUTF8))


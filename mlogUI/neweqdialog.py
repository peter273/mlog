# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'neweq.ui'
#
# Created: Sun Mar 19 15:00:29 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(239, 177)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 130, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 108))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.eqName_lineedit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.eqName_lineedit.setText("")
        self.eqName_lineedit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.eqName_lineedit.setObjectName("eqName_lineedit")
        self.verticalLayout.addWidget(self.eqName_lineedit)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.eqtype_combobox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.eqtype_combobox.setObjectName("eqtype_combobox")
        self.eqtype_combobox.addItem("")
        self.eqtype_combobox.addItem("")
        self.verticalLayout.addWidget(self.eqtype_combobox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "New Equipment", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Input Equipment Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Equipment Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.eqtype_combobox.setItemText(0, QtGui.QApplication.translate("Dialog", "Shovel", None, QtGui.QApplication.UnicodeUTF8))
        self.eqtype_combobox.setItemText(1, QtGui.QApplication.translate("Dialog", "Truck", None, QtGui.QApplication.UnicodeUTF8))


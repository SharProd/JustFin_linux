# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\JustFin\dialog_with_button.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogB(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 250)
        Dialog.setStyleSheet("background-color: rgb(90, 90, 90);\n"
"color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\JustFin\\icon/allert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(15)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet(" QPushButton {\n"
"     color: rgb(232, 232, 232);\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: rgb(49, 49, 49);\n"
"     min-width: 100px;\n"
" }\n"
"QPushButton:hover{\n"
"    color: rgb(49, 49, 49);\n"
"    background-color: rgb(190, 190, 190);\n"
"}\n"
"\n"
" QPushButton:pressed {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"     background-color: rgb(91, 91, 91);\n"
" }\n"
"\n"
" QPushButton:flat {\n"
"     border: none; /* для плоской кнопки границы нет */\n"
" }\n"
"")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
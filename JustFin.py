# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\JustFin\JustFin.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(518, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/37533/Downloads/free-icon-wallet-2142541.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget.setObjectName("centralwidget")
        self.main_view = QtWidgets.QTabWidget(self.centralwidget)
        self.main_view.setEnabled(True)
        self.main_view.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.main_view.setMinimumSize(QtCore.QSize(500, 500))
        self.main_view.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.main_view.setFont(font)
        self.main_view.setToolTip("")
        self.main_view.setStyleSheet("alternate-background-color: rgb(0, 170, 127);\n"
"background-color: rgb(49, 49, 49);")
        self.main_view.setObjectName("main_view")
        self.main = QtWidgets.QWidget()
        self.main.setToolTip("")
        self.main.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"alternate-background-color: rgb(49, 49, 49);")
        self.main.setObjectName("main")
        self.splitter = QtWidgets.QSplitter(self.main)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 300, 22))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.main)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 34, 351, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(232, 232, 232);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.earned_in_mounth = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.earned_in_mounth.setFont(font)
        self.earned_in_mounth.setStyleSheet("color: rgb(232, 232, 232);")
        self.earned_in_mounth.setObjectName("earned_in_mounth")
        self.horizontalLayout_3.addWidget(self.earned_in_mounth)
        self.currency_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.currency_1.setFont(font)
        self.currency_1.setStyleSheet("color: rgb(232, 232, 232);")
        self.currency_1.setObjectName("currency_1")
        self.horizontalLayout_3.addWidget(self.currency_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(232, 232, 232);")
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.money_in_mounth = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.money_in_mounth.setFont(font)
        self.money_in_mounth.setStyleSheet("color: rgb(232, 232, 232);")
        self.money_in_mounth.setObjectName("money_in_mounth")
        self.horizontalLayout_10.addWidget(self.money_in_mounth)
        self.currency_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.currency_2.setFont(font)
        self.currency_2.setStyleSheet("color: rgb(232, 232, 232);")
        self.currency_2.setObjectName("currency_2")
        self.horizontalLayout_10.addWidget(self.currency_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(232, 232, 232);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.get_money = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_money.setFont(font)
        self.get_money.setStyleSheet("color: rgb(232, 232, 232);")
        self.get_money.setObjectName("get_money")
        self.horizontalLayout_5.addWidget(self.get_money)
        self.currency_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.currency_3.setFont(font)
        self.currency_3.setStyleSheet("color: rgb(232, 232, 232);")
        self.currency_3.setObjectName("currency_3")
        self.horizontalLayout_5.addWidget(self.currency_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(232, 232, 232);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.expenses_in_mounth = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.expenses_in_mounth.setFont(font)
        self.expenses_in_mounth.setStyleSheet("color: rgb(232, 232, 232);")
        self.expenses_in_mounth.setObjectName("expenses_in_mounth")
        self.horizontalLayout_8.addWidget(self.expenses_in_mounth)
        self.currency_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.currency_5.setFont(font)
        self.currency_5.setStyleSheet("color: rgb(232, 232, 232);")
        self.currency_5.setObjectName("currency_5")
        self.horizontalLayout_8.addWidget(self.currency_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.layoutWidget1 = QtWidgets.QWidget(self.main)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 420, 441, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.date_progress = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_progress.setFont(font)
        self.date_progress.setStyleSheet("color: rgb(232, 232, 232);")
        self.date_progress.setObjectName("date_progress")
        self.horizontalLayout_7.addWidget(self.date_progress)
        self.main_view.addTab(self.main, "")
        self.Edit_day = QtWidgets.QWidget()
        self.Edit_day.setToolTip("")
        self.Edit_day.setWhatsThis("")
        self.Edit_day.setObjectName("Edit_day")
        self.layoutWidget2 = QtWidgets.QWidget(self.Edit_day)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.layoutWidget2)
        self.line.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget2)
        self.line_2.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.earned_text = QtWidgets.QLabel(self.layoutWidget2)
        self.earned_text.setMinimumSize(QtCore.QSize(20, 20))
        self.earned_text.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        self.earned_text.setFont(font)
        self.earned_text.setStyleSheet("color:rgb(255, 255, 255)")
        self.earned_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.earned_text.setIndent(10)
        self.earned_text.setObjectName("earned_text")
        self.horizontalLayout.addWidget(self.earned_text)
        self.sum_1 = QtWidgets.QLabel(self.layoutWidget2)
        self.sum_1.setMinimumSize(QtCore.QSize(50, 0))
        self.sum_1.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        self.sum_1.setFont(font)
        self.sum_1.setStyleSheet("color:rgb(255, 255, 255)")
        self.sum_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sum_1.setIndent(0)
        self.sum_1.setObjectName("sum_1")
        self.horizontalLayout.addWidget(self.sum_1)
        self.currency_edit_earner = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currency_edit_earner.setFont(font)
        self.currency_edit_earner.setStyleSheet("color:rgb(255, 255, 255)")
        self.currency_edit_earner.setObjectName("currency_edit_earner")
        self.horizontalLayout.addWidget(self.currency_edit_earner)
        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.expensese_text = QtWidgets.QLabel(self.layoutWidget2)
        self.expensese_text.setMinimumSize(QtCore.QSize(20, 20))
        self.expensese_text.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        self.expensese_text.setFont(font)
        self.expensese_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.expensese_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.expensese_text.setIndent(10)
        self.expensese_text.setObjectName("expensese_text")
        self.horizontalLayout_2.addWidget(self.expensese_text)
        self.sum_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.sum_2.setMinimumSize(QtCore.QSize(50, 0))
        self.sum_2.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        self.sum_2.setFont(font)
        self.sum_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.sum_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sum_2.setIndent(0)
        self.sum_2.setObjectName("sum_2")
        self.horizontalLayout_2.addWidget(self.sum_2)
        self.currency_edit_expenses = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currency_edit_expenses.setFont(font)
        self.currency_edit_expenses.setStyleSheet("color:rgb(255, 255, 255)")
        self.currency_edit_expenses.setObjectName("currency_edit_expenses")
        self.horizontalLayout_2.addWidget(self.currency_edit_expenses)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sum_edit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.sum_edit.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sum_edit.setFont(font)
        self.sum_edit.setStyleSheet("QLineEdit {\n"
"     border: none;\n"
"     border-radius: 8px;\n"
"     selection-background-color:rgb(232, 232, 232);\n"
"    color:rgb(255, 255, 255);\n"
" }")
        self.sum_edit.setMaxLength(5)
        self.sum_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.sum_edit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.sum_edit.setObjectName("sum_edit")
        self.gridLayout.addWidget(self.sum_edit, 0, 2, 1, 1)
        self.currency_Box2 = QtWidgets.QComboBox(self.layoutWidget2)
        self.currency_Box2.setMinimumSize(QtCore.QSize(60, 25))
        self.currency_Box2.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.currency_Box2.setFont(font)
        self.currency_Box2.setStyleSheet("color: rgb(232, 232, 232);\n"
"border:none;")
        self.currency_Box2.setObjectName("currency_Box2")
        self.currency_Box2.addItem("")
        self.currency_Box2.addItem("")
        self.currency_Box2.addItem("")
        self.gridLayout.addWidget(self.currency_Box2, 0, 3, 1, 1)
        self.comments_edit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.comments_edit.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comments_edit.setFont(font)
        self.comments_edit.setStyleSheet("\n"
"QLineEdit {\n"
"     border: none;\n"
"     border-radius: 8px;\n"
"     selection-background-color:rgb(232, 232, 232);\n"
"    color:rgb(255, 255, 255);\n"
" }\n")
        self.comments_edit.setInputMask("")
        self.comments_edit.setText("")
        self.comments_edit.setMaxLength(20)
        self.comments_edit.setFrame(False)
        self.comments_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.comments_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.comments_edit.setDragEnabled(False)
        self.comments_edit.setObjectName("comments_edit")
        self.gridLayout.addWidget(self.comments_edit, 0, 1, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.layoutWidget2)
        self.save_button.setMinimumSize(QtCore.QSize(84, 25))
        self.save_button.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet(" QPushButton {\n"
"     color: rgb(232, 232, 232);\n"
"    border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: rgb(49, 49, 49);\n"
"     min-width: 80px;\n"
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
"     border: none; /* ?????? ?????????????? ???????????? ?????????????? ?????? */\n"
" }\n"
"\n"
"")
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 0, 4, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color: rgb(232, 232, 232);")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.layoutWidget2)
        self.calendarWidget.setMinimumSize(QtCore.QSize(450, 0))
        self.calendarWidget.setMaximumSize(QtCore.QSize(480, 16777215))
        self.calendarWidget.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"color: rgb(232, 232, 232);\n"
"alternate-background-color: rgb(49, 49, 49);\n"
"selection-color: rgb(49, 49, 49);\n"
"selection-background-color: rgb(190, 190, 190);\n"
"")
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_2.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("color: rgb(232, 232, 232);\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_2)
        self.show_day_list = QtWidgets.QPushButton(self.layoutWidget2)
        self.show_day_list.setMinimumSize(QtCore.QSize(84, 25))
        self.show_day_list.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.show_day_list.setFont(font)
        self.show_day_list.setStyleSheet(" QPushButton {\n"
"     color: rgb(232, 232, 232);\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: rgb(49, 49, 49);\n"
"     min-width: 80px;\n"
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
"     border: none; /* ?????? ?????????????? ???????????? ?????????????? ?????? */\n"
" }\n"
"")
        self.show_day_list.setObjectName("show_day_list")
        self.horizontalLayout_9.addWidget(self.show_day_list)
        self.show_mounth_list = QtWidgets.QPushButton(self.layoutWidget2)
        self.show_mounth_list.setEnabled(True)
        self.show_mounth_list.setMinimumSize(QtCore.QSize(84, 25))
        self.show_mounth_list.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.show_mounth_list.setFont(font)
        self.show_mounth_list.setStyleSheet(" QPushButton {\n"
"     color: rgb(232, 232, 232);\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: rgb(49, 49, 49);\n"
"     min-width: 80px;\n"
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
"     border: none; /* ?????? ?????????????? ???????????? ?????????????? ?????? */\n"
" }\n"
"")
        self.show_mounth_list.setObjectName("show_mounth_list")
        self.horizontalLayout_9.addWidget(self.show_mounth_list)
        self.clear_list = QtWidgets.QPushButton(self.layoutWidget2)
        self.clear_list.setMinimumSize(QtCore.QSize(84, 25))
        self.clear_list.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.clear_list.setFont(font)
        self.clear_list.setStyleSheet(" QPushButton {\n"
"     color: rgb(232, 232, 232);\n"
"     border: 2px solid #8f8f91;\n"
"     border-radius: 6px;\n"
"     background-color: rgb(49, 49, 49);\n"
"     min-width: 80px;\n"
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
"     border: none; /* ?????? ?????????????? ???????????? ?????????????? ?????? */\n"
" }\n"
"")
        self.clear_list.setObjectName("clear_list")
        self.horizontalLayout_9.addWidget(self.clear_list)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.main_view.addTab(self.Edit_day, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusbar.setStyleSheet("color: rgb(232, 232, 232);\n"
"")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.main_view.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comments_edit, self.sum_edit)
        MainWindow.setTabOrder(self.sum_edit, self.main_view)
        MainWindow.setTabOrder(self.main_view, self.currency_Box2)
        MainWindow.setTabOrder(self.currency_Box2, self.calendarWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JustFin"))
        self.label_2.setText(_translate("MainWindow", "?????????????????? ???? ?????????? :"))
        self.earned_in_mounth.setText(_translate("MainWindow", "0"))
        self.currency_1.setText(_translate("MainWindow", "BYN"))
        self.label.setText(_translate("MainWindow", "???? ???? ?????????? :"))
        self.money_in_mounth.setText(_translate("MainWindow", "0"))
        self.currency_2.setText(_translate("MainWindow", "BYN"))
        self.label_9.setText(_translate("MainWindow", "???????????????? ?????????? ???? :"))
        self.get_money.setText(_translate("MainWindow", "0"))
        self.currency_3.setText(_translate("MainWindow", "BYN"))
        self.label_6.setText(_translate("MainWindow", "???????????????? ???? ?????????? :"))
        self.expenses_in_mounth.setText(_translate("MainWindow", "0"))
        self.currency_5.setText(_translate("MainWindow", "BYN"))
        self.date_progress.setText(_translate("MainWindow", "01.01.2020"))
        self.main_view.setTabText(self.main_view.indexOf(self.main), _translate("MainWindow", "Main"))
        self.earned_text.setText(_translate("MainWindow", "?????????????????? :"))
        self.sum_1.setText(_translate("MainWindow", "0"))
        self.currency_edit_earner.setText(_translate("MainWindow", "BYN"))
        self.expensese_text.setText(_translate("MainWindow", "???????????????? :"))
        self.sum_2.setText(_translate("MainWindow", "0"))
        self.currency_edit_expenses.setText(_translate("MainWindow", "BYN"))
        #self.sum_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">?????????????? ?????????????????????</span></p></body></html>"))
        self.sum_edit.setPlaceholderText(_translate("MainWindow", "??????????"))
       # self.currency_Box2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">???????????? ???????????????? ????????????-????????????</span></p></body></html>"))
        self.currency_Box2.setItemText(0, _translate("MainWindow", "BYN"))
        self.currency_Box2.setItemText(1, _translate("MainWindow", "USD"))
        self.currency_Box2.setItemText(2, _translate("MainWindow", "EUR"))
        #self.comments_edit.setToolTip(_translate("MainWindow", "<html><head/><body><p>?????? ???????????????? ?????? ???? ?????? ?????????????????<br/></p></body></html>"))
        self.comments_edit.setPlaceholderText(_translate("MainWindow", "?????? ?????????????"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        #self.calendarWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">???????????????? ???????? ?????? ???????????????????????????? ???????????????? ????????????-????????????.</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "?????????????? ??????"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "????????????????"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "??????????????"))
        self.show_day_list.setText(_translate("MainWindow", "???????????????????? ????????????"))
        self.show_mounth_list.setText(_translate("MainWindow", "???????????? ???? ????????????"))
        self.clear_list.setText(_translate("MainWindow", "????????????????"))
        self.main_view.setTabText(self.main_view.indexOf(self.Edit_day), _translate("MainWindow", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

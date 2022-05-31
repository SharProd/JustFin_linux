from JustFin import Ui_MainWindow
from Scroll_QT import Ui_Dialog_scroll
from dialog import Ui_Dialog
from dialog_with_button import Ui_DialogB
from scrollQT import Ui_Dialog_mounth_list
from PyQt5 import QtCore, QtGui, QtWidgets
from dialog_log import Ui_Dialog_log
import sys
from datetime import date,time,datetime
import os

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
Dialog = QtWidgets.QDialog()
info_ui = Ui_Dialog()
info_ui.setupUi(Dialog)
appB = QtWidgets.QApplication(sys.argv)
DialogB = QtWidgets.QDialog()
ui_B = Ui_DialogB()
ui_B.setupUi(DialogB)
Dialog_scroll = QtWidgets.QDialog()
ui_scroll = Ui_Dialog_scroll()
ui_scroll.setupUi(Dialog_scroll)
Dialog_log = QtWidgets.QDialog()
ui_log = Ui_Dialog_log()
ui_log.setupUi(Dialog_log)
Dialog_mounth_list = QtWidgets.QDialog()
ui_mounth_list = Ui_Dialog_mounth_list()
ui_mounth_list.setupUi(Dialog_mounth_list)
app_mounth = QtWidgets.QApplication(sys.argv)
MainWindow.show()


ui.dateEdit.setDate(date.today())
date_today = date.today()
date_today = date_today.strftime('%d.%B.%Y')
ui.date_progress.setText(date_today)

#создание папки с файлами записи и файлов записи


if not os.path.isdir("libr"):
	os.mkdir("libr")
with open("libr/day_dict.txt",'a+'):
	pass
with open("libr/expenses_dict.txt",'a+'):
	pass
with open("libr/money_dict.txt",'a+'):
	pass

day_dict = dict()
expenses_dict = dict()
money_dict = dict()
date_work = ui.dateEdit.date().toString('dd.MM.yyyy')
comment = ui.comments_edit.text()
money = ui.sum_edit.text()


class add_day():
	def __init__(self,date,place,money):
		self.date_day = date
		self.place_day = place
		self.money = money
		global day_dict
		with open("libr/day_dict.txt",'r') as file:
			a = file.read()
			if a!='':
				a = eval(a)
				day_dict = a
			else:
				pass
		if self.date_day in day_dict:
			ui.statusbar.showMessage(f'День изменен - {self.date_day} - {self.place_day} - {self.money}',5000)	
		else:
			ui.statusbar.showMessage(f'День добавлен - {self.date_day} - {self.place_day} - {self.money}',5000)
		day_dict[self.date_day] = [self.place_day,self.money]
		with open("libr/day_dict.txt",'w+') as file:
			file.write(str(day_dict))
		mounth_list_edit(0)
		sum_get_money()	
		show_values_in_mounth()
			
		#print('ADD_DAY\nсоздан обьект класса add_day для добавления дня в список ')
		
class add_money():
	def __init__(self,date,place,money):
		self.date_day = date
		self.place_day = place
		self.money = money
		global money_dict
		with open("libr/money_dict.txt",'r') as file:
			a = file.read()
			if a!="":
				a = eval(a)
				money_dict = a
			else:
				pass
		if self.date_day in money_dict:
			ui.statusbar.showMessage(f'Деньги изменены - {self.date_day} - {self.place_day} - {self.money}',5000)	
		else:
			ui.statusbar.showMessage(f'Деньги добавлены - {self.date_day} - {self.place_day} - {self.money}',5000)
		money_dict[self.date_day] = [self.place_day,self.money]
		with open("libr/money_dict.txt",'w+') as file:
			file.write(str(money_dict))			
		mounth_list_edit(0)
		sum_get_money()	
		show_values_in_mounth()

class add_expenses():
	def __init__(self,date,place,money):
		self.date_day = date
		self.place_day = place
		self.money = money
		global expenses_dict
		with open("libr/expenses_dict.txt",'r') as file:
			a = file.read()
			if a!="":
				a = eval(a)
				expenses_dict = a
			else:
				pass
		if self.date_day in expenses_dict:
			ui.statusbar.showMessage(f'Pacходы изменены - {self.date_day} - {self.place_day} - {self.money}',5000)	
		else:
			ui.statusbar.showMessage(f'Дасходы добавлены - {self.date_day} - {self.place_day} - {self.money}',5000)
		expenses_dict[self.date_day] = [self.place_day,self.money]
		with open("libr/expenses_dict.txt",'w+') as file:
			file.write(str(expenses_dict))	
		mounth_list_edit(0)		
		show_values_in_mounth()	

class mounth_list():
	def __init__(self):
		pass

def add_or_edit_day_and_money():
	date_work = ui.dateEdit.date().toString('dd.MM.yyyy')
	comment = ui.comments_edit.text()
	money = ui.sum_edit.text()
	global day_dict
	if ui.currency_Box2.currentIndex()==1:
		x = float(money)
		money = x*2.5
	if ui.currency_Box2.currentIndex()==2:
		x = float(money)
		money = x*2.93
	if ui.comboBox_2.currentIndex()==0:
		name_file = "libr/day_dict.txt" 
	if ui.comboBox_2.currentIndex()==1:
		name_file = "libr/money_dict.txt"
	if ui.comboBox_2.currentIndex()==2:
		name_file = "libr/expenses_dict.txt"

	with open(name_file,'r') as file:
			a = file.read()
			if a!='':
				a = eval(a)
				day_dict = a 			
				if date_work in day_dict:
					DialogB.show()
					ui_B.label.setText('День будет изменен?')
					ui_B.buttonBox.rejected.connect(no_save)
					ui_B.buttonBox.accepted.connect(save)
				else:
					if ui.comboBox_2.currentIndex()==0:
						day = add_day(date_work,comment,money)
					if ui.comboBox_2.currentIndex()==1:
						day = add_money(date_work,comment,money)
					if ui.comboBox_2.currentIndex()==2:
						day = add_expenses(date_work,comment,money)												
					ui.comments_edit.clear()
					ui.sum_edit.clear()
			else:
					if ui.comboBox_2.currentIndex()==0:
						day = add_day(date_work,comment,money)
					if ui.comboBox_2.currentIndex()==1:
						day = add_money(date_work,comment,money)
					if ui.comboBox_2.currentIndex()==2:
						day = add_expenses(date_work,comment,money)												
					ui.comments_edit.clear()
					ui.sum_edit.clear()

#сохранение дня при изменении, выбор в диалоговом окне
def save():
	date_work = ui.dateEdit.date().toString('dd.MM.yyyy')
	comment = ui.comments_edit.text()
	money = ui.sum_edit.text()
	if (money and comment) != '':
			money = int(money)
			if ui.comboBox_2.currentIndex()==0:
				day = add_day(date_work,comment,money)
			if ui.comboBox_2.currentIndex()==1:
				day = add_money(date_work,comment,money)
			if ui.comboBox_2.currentIndex()==2:
				day = add_expenses(date_work,comment,money)
			
	DialogB.close()
	ui.comments_edit.clear()
	ui.sum_edit.clear()

def no_save():
	DialogB.close()
#изменение даты из календаря
def date_edit():
	ui.dateEdit.setDate(ui.calendarWidget.selectedDate())

def show_values_in_mounth():
	value_day = 0
	value_money = 0
	value_expenses = 0
	mounth = date.today()
	mounth = mounth.strftime('%B_%Y')
	try:
		with open(f"libr/mounth/day_dict{mounth}.txt",'r') as file:
			s = file.readlines()
			for i in s:
				i = i[-10:-6]
				value_day += eval(i)
		with open(f"libr/mounth/money_dict{mounth}.txt",'r') as file:
			s = file.readlines()
			for i in s:
				i = i[-10:-6]
				value_money += eval(i)
		with open(f"libr/mounth/expenses_dict{mounth}.txt",'r') as file:
			s = file.readlines()
			for i in s:
				i = i[-10:-6]
				value_expenses += eval(i)
	except FileNotFoundError:
		pass
	ui.earned_in_mounth.setText(str(value_day))
	ui.sum_1.setText(str(value_day))
	ui.money_in_mounth.setText(str(value_money))
	ui.sum_2.setText(str(value_expenses))
	ui.expenses_in_mounth.setText(str(value_expenses))	

def sum_get_money():
	sum_day = 0
	sum_money = 0
	with open("libr/day_dict.txt",'r') as file:
		a = file.read()
		if a!='':
			a = eval(a)
			day_dict = a
			for i in day_dict.values():
				sum_day+=int(i[1])
	with open("libr/money_dict.txt",'r') as file:
		a = file.read()
		if a!='':
			a = eval(a)
			day_dict = a
			for i in day_dict.values():
				sum_money+=int(i[1])
	value = sum_day - sum_money		
	ui.get_money.setText(str(value))
	
def clicked_save():
	date_work = ui.dateEdit.date().toString('dd.MM.yyyy')
	comment = ui.comments_edit.text()
	money = ui.sum_edit.text()
	if (money and comment) != '':
		try:
			money = int(money)
			add_or_edit_day_and_money()
			#ui.comments_edit.clear()
			#ui.sum_edit.clear()
		except ValueError:
			Dialog.setWindowTitle('ОШИБКА!')
			info_ui.label.setText('В строке "сумма" \nвведите ЧИСЛО!')
			Dialog.show()
	else:
		ui.statusbar.showMessage('Не все поля заполнены!')

def show_dict():
	name_file = ''
	all_money = ''
	write_label = ''
	itogo = 0 
	sum_day = 0
	if ui.comboBox_2.currentIndex()==0:
		name_file ="libr/day_dict.txt"
		all_money = "Всего заработано: "
	if ui.comboBox_2.currentIndex()==1:
		name_file ="libr/money_dict.txt"
		all_money = "Всего получено: "
		need_money = "Еще должны: "
	if ui.comboBox_2.currentIndex()==2:
		name_file ="libr/expenses_dict.txt"
		all_money = "Всего потрачено: "

	with open("libr/day_dict.txt",'r') as file:
		a = file.read()
		if a!='':
			a = eval(a)
			day_dict = a
			l = []
			obj = day_dict.keys()
			for j in obj:
				dat = j
				date_obj = datetime.strptime(dat, '%d.%m.%Y')
				l.append(date_obj)
			for i in sorted(l):
				long_date = i.strftime('%d - %a - %B %Y')
				i = i.strftime('%d.%m.%Y')
				sum_day+=int(day_dict[i][1])
	
	with open(name_file,'r') as file:
		a = file.read()
		if a!='':
			a = eval(a)
			day_dict = a
			l = []
			obj = day_dict.keys()
			for j in obj:
				dat = j
				date_obj = datetime.strptime(dat, '%d.%m.%Y')
				l.append(date_obj)
			Dialog_scroll.setWindowTitle(ui.comboBox_2.currentText())
			Dialog_scroll.show()
			for i in sorted(l):
				long_date = i.strftime('%d - %a - %B %Y')
				i = i.strftime('%d.%m.%Y')
				write_label += f'{long_date:<28}|{day_dict[i][0]:^20}|{day_dict[i][1]:>5} BYN\n'
				itogo+=int(day_dict[i][1])
			write_label+=f"\n\n{all_money} {itogo} BYN"
			if ui.comboBox_2.currentIndex()==1:
				write_label+=f"\n{need_money}{sum_day-itogo} BYN"

			ui_scroll.view_day_list.setText(write_label)

		else:
			Dialog.setWindowTitle('Ошибка!')
			info_ui.label.setText('Опаньки, вы еще ничего не записали!!!')
			Dialog.show()

def mounth_list_edit(value=1):

	mounth_in_comboBox = list()
	global mounth_object
	mounth_object = mounth_list()
	mounth_object.mounth_dict = dict()
	mounth_object.mounth_value = dict()
	name_file_list = ["libr/day_dict.txt","libr/money_dict.txt","libr/expenses_dict.txt"]
	name_file = ''
	if value == 1:
		if ui.comboBox_2.currentIndex()==0:
			name_file ="libr/day_dict.txt"
		if ui.comboBox_2.currentIndex()==1:
			name_file ="libr/money_dict.txt"
		if ui.comboBox_2.currentIndex()==2:
			name_file ="libr/expenses_dict.txt"
		with open(name_file,'r') as file:
			a = file.read()
			if a!='':
				a = eval(a)
				day_dict = a
				l = []
				obj = day_dict.keys()
				for j in obj:
					dat = j
					date_obj = datetime.strptime(dat, '%d.%m.%Y')
					l.append(date_obj)
				write_label = ''
				itogo = 0
				if not os.path.isdir("libr/mounth"):
					os.mkdir("libr/mounth")
				for i in sorted(l):
					mounth = i.strftime('%B_%Y')
					if ui.comboBox_2.currentIndex()==0:
						name_file = f"libr/mounth/day_dict{mounth}.txt"
						with open(name_file,'w') as file:
							file.write('')
					if ui.comboBox_2.currentIndex()==1:
						name_file = f"libr/mounth/money_dict{mounth}.txt"
						with open(name_file,'w') as file:
							file.write('')
					if ui.comboBox_2.currentIndex()==2:
						name_file = f"libr/mounth/expenses_dict{mounth}.txt"	
						with open(name_file,'w') as file:
							file.write('')	
				for i in sorted(l):
					mounth = i.strftime('%B_%Y')
					if ui.comboBox_2.currentIndex()==0:
						name_file = f"libr/mounth/day_dict{mounth}.txt"
					if ui.comboBox_2.currentIndex()==1:
						name_file = f"libr/mounth/money_dict{mounth}.txt"
					if ui.comboBox_2.currentIndex()==2:
						name_file = f"libr/mounth/expenses_dict{mounth}.txt"	
					long_date = i.strftime('%d - %a - %B %Y')
					i = i.strftime('%d.%m.%Y')
					write_label = f'{long_date:<28}|{day_dict[i][0]:^20}|{day_dict[i][1]:<5} BYN\n'
					if f'{mounth}' in mounth_object.mounth_dict.keys():
						mounth_object.mounth_dict[f'{mounth}'] += int(day_dict[i][1])
					else:
						mounth_object.mounth_dict[f'{mounth}'] = int(day_dict[i][1])
					if f'{mounth}' in mounth_object.mounth_value:
						mounth_object.mounth_value[f'{mounth}'] += (write_label)
					else:
						mounth_object.mounth_value[f'{mounth}'] = (write_label)

					with open(name_file,'a') as file:
						file.write(write_label)
				if value == 1:
					create_item_comboBox()
			else:
				Dialog.setWindowTitle('Ошибка!')
				info_ui.label.setText('Опаньки, вы еще ничего не записали!!!')
				Dialog.show()	
	if value == 0:
		for name_file in name_file_list:
			with open(name_file,'r') as file:
				a = file.read()
				if a!='':
					a = eval(a)
					day_dict = a
					l = []
					obj = day_dict.keys()
					for j in obj:
						dat = j
						date_obj = datetime.strptime(dat, '%d.%m.%Y')
						l.append(date_obj)
					write_label = ''
					itogo = 0
					if not os.path.isdir("libr/mounth"):
						os.mkdir("libr/mounth")
					
					for i in sorted(l):
						mounth = i.strftime('%B_%Y')
						if name_file ==	"libr/day_dict.txt":
							with open(f"libr/mounth/day_dict{mounth}.txt",'w') as file:
								file.write('')
						if name_file ==	"libr/money_dict.txt":
							with open(f"libr/mounth/money_dict{mounth}.txt",'w') as file:
								file.write('')
						if name_file ==	"libr/expenses_dict.txt":
							with open(f"libr/mounth/expenses_dict{mounth}.txt",'w') as file:
								file.write('')														
					for i in sorted(l):
						mounth = i.strftime('%B_%Y')
						long_date = i.strftime('%d - %a - %B %Y')
						i = i.strftime('%d.%m.%Y')
						write_label = f'{long_date:<28}|{day_dict[i][0]:^20}|{day_dict[i][1]:<5} BYN\n'
						if f'{mounth}' in mounth_object.mounth_dict.keys():
							mounth_object.mounth_dict[f'{mounth}'] += int(day_dict[i][1])
						else:
							mounth_object.mounth_dict[f'{mounth}'] = int(day_dict[i][1])
						if f'{mounth}' in mounth_object.mounth_value:
							mounth_object.mounth_value[f'{mounth}'] += (write_label)
						else:
							mounth_object.mounth_value[f'{mounth}'] = (write_label)
						if name_file ==	"libr/day_dict.txt":
							with open(f"libr/mounth/day_dict{mounth}.txt",'a') as file:
								file.write(write_label)
						if name_file ==	"libr/money_dict.txt":
							with open(f"libr/mounth/money_dict{mounth}.txt",'a') as file:
								file.write(write_label)
						if name_file ==	"libr/expenses_dict.txt":
							with open(f"libr/mounth/expenses_dict{mounth}.txt",'a') as file:
								file.write(write_label)																
					if value == 1:
						create_item_comboBox()	

def clear_dict():

	if ui.comboBox_2.currentIndex()==0:
		name_file ="libr/day_dict.txt"
	if ui.comboBox_2.currentIndex()==1:
		name_file ="libr/money_dict.txt"
	if ui.comboBox_2.currentIndex()==2:
		name_file ="libr/expenses_dict.txt"

	date_work = ui.dateEdit.date().toString('dd.MM.yyyy')
	with open(name_file,'r') as file:
		a = file.read()
		if a!='':
			a = eval(a)
			day_dict = a
			if date_work in day_dict:
				DialogB.setWindowTitle('Внимание!')
				ui_B.label.setText('Вы ействительно хотите удалить день?')
				DialogB.show()	
				ui_B.buttonBox.rejected.connect(clear_no)
				ui_B.buttonBox.accepted.connect(clear_yes)
			else:
				ui.statusbar.showMessage(f'Такого дня нет в журнале!',5000)

def clear_yes():
	if ui.comboBox_2.currentIndex()==0:
		name_file ="libr/day_dict.txt"
	if ui.comboBox_2.currentIndex()==1:
		name_file ="libr/money_dict.txt"
		all_money = "Всего получено: "
	if ui.comboBox_2.currentIndex()==2:
		name_file ="libr/expenses_dict.txt"
	date_work = ui.dateEdit.date().toString('dd.MM.yyyy')
	with open(name_file,'r') as file:
		a = file.read()
		if a!='':
			a = eval(a)
			day_dict = a
			try:
				del day_dict[date_work]
			except KeyError:
				pass

			ui.statusbar.showMessage(f'День удален - {date_work}',5000)
			with open(name_file,'w') as file:
				file.write(str(day_dict))
	mounth_list_edit(0)
	sum_get_money()
	DialogB.close()
	show_values_in_mounth()
def clear_no():
	DialogB.close()

def create_item_comboBox():
	if len(ui_mounth_list.comboBox_2)==0:
		for i in mounth_object.mounth_dict.keys():
			if ui.comboBox_2.currentIndex()==0:
				name_file = f"libr/mounth/day_dict{i}.txt"
			if ui.comboBox_2.currentIndex()==1:
				name_file = f"libr/mounth/money_dict{i}.txt"
			if ui.comboBox_2.currentIndex()==2:
				name_file = f"libr/mounth/expenses_dict{i}.txt"
			with open(name_file,'a') as file:
				file.write(f'\n\nВсего: {mounth_object.mounth_dict[i]}')
				ui_mounth_list.comboBox_2.addItem(i)
		Dialog_mounth_list.setWindowTitle(ui.comboBox_2.currentText())		
		Dialog_mounth_list.show()
		ui_mounth_list.comboBox_2.currentTextChanged.connect(create_combobox_label_text)
		if len(ui_mounth_list.comboBox_2)!=0:
			ui_mounth_list.label.setText(f'{mounth_object.mounth_value[ui_mounth_list.comboBox_2.currentText()]}\n\nВсего : {mounth_object.mounth_dict[ui_mounth_list.comboBox_2.currentText()]}')
	elif len(ui_mounth_list.comboBox_2)!= 0:
		ui_mounth_list.comboBox_2.clear()
		create_item_comboBox()
	
def create_combobox_label_text():
	if len(ui_mounth_list.comboBox_2)!=0:
		ui_mounth_list.label.setText(f'{mounth_object.mounth_value[ui_mounth_list.comboBox_2.currentText()]}\n\nВсего : {mounth_object.mounth_dict[ui_mounth_list.comboBox_2.currentText()]}')


ui.save_button.clicked.connect(clicked_save)
ui.calendarWidget.clicked.connect(date_edit)
ui.show_day_list.clicked.connect(show_dict)
ui.show_mounth_list.pressed.connect(mounth_list_edit)
ui.clear_list.clicked.connect(clear_dict)



mounth_list_edit(0)
sum_get_money()
show_values_in_mounth()
sys.exit(app.exec_())

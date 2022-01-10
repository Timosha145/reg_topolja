from random import *
from module1 import *
passwords=['Username123!']
usernames=['Username']

answerReg=''
answerAboutPass=''
passTry=1
cor=''
a=False


while answerReg not in ['y','n','Y','N']:
	answerReg=input('Добро пожаловать! Вы уже зарегистрированы?(y/n): ')
if answerReg in ['N','n']:
	while a==False:
		newUser=input('Придумайте себе имя пользователя не длинне 12 символов: ')
		if len(newUser)>12:
			print('В имени больше 12 символов!')
		elif isUserUnic(usernames,newUser)==False:
			print('Такой пользователь уже существует')	
		elif isUserUnic(usernames,newUser)==True and len(newUser)<=12:
			break
	answer=''
	while answerAboutPass not in ['y','n','Y','N']:
		answerAboutPass=input('Желаете авто генерацию пороля?(y/n): ')
	while 1:
		if passTry==0 and answerAboutPass in ['n','N']:
			break
		elif answerAboutPass in ['y','Y']:
			newPass=autoPassGenerator()
			print('Ваш пароль -',newPass)
			answer=''
			while answer not in ['y','n','Y','N']:
				answer=input(f'Перегенирировать пароль?(y/n): ')
			if answer in ['n','N']:
				break
		while passTry==1 and answerAboutPass in ['n','N']:
			if answerAboutPass in ['n','N']:
				newPass=input('Придумайте новый пароль для данного пользователя, которое будет содержать цифры, буквы нижнего и верхнего регистра, а также спец символы и будет содержать минимум 8 символов: ')
			if isPassOkay(newPass)==False:
				print('К сожалению пароль не подходит')
			else: 
				while 1:
					passAgain=input('Подтвердите ваш новый пароль: ')
					if passAgain==newPass:
						passTry=0
						break
					else:
						print('К сожалению пароли не совпадают')
						while answer not in ['y','n','Y','N']:
							tryAgain=input('Желайте придумать новый пароль?(y/n): ')
						if tryAgain in ['y','Y']:
							break
if answerReg in ['N','n']:
	usernames.append(newUser)
	passwords.append(newPass)
print()
print('Для подтверждения просим пройти этап авторизации')
while 1:
	logUsername=input('Введите ваше имя пользователя: ')
	logPassword=input('Введите ваш пароль: ')
	try:
		cor=isUserCorrect(logUsername, logPassword, usernames, passwords)
	except ValueError:
		print('Упс что-то пошло не так')
	if cor==True:
		break
print('Добро пожаловать в систему!')

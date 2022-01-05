from random import *
from module1 import *
passwords=['Password789!']
usernames=['Boris1']

answer=''
answerAboutPass=''
a=False


while answer not in ['y','n','Y','N']:
	answer=input('Добро пожаловать! Вы уже зарегистрированы?(y/n): ')
if answer in ['N','n']:
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
		if answerAboutPass in ['y','Y']:
			print('Ваш пароль -',autoPassGenerator())
			answer=''
			while answer not in ['y','n','Y','N']:
				answer=input(f'Перегенирировать пароль?(y/n): ')
			if answer in ['n','N']:
				break
		while 1:
			if answerAboutPass in ['n','N']:
				newPass=input('Придумайте новый пароль для данного пользователя, которое будет содержать цифры, буквы нижнего и верхнего регистра, а также спец символы: ')
			if isPassOkay(newPass)==True:
				print('К сожалению пароль не подходит')
			else: print('Ваш пароль',)

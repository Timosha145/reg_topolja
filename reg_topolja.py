from random import *
from module1 import *
passwords=['Password789!']
usernames=['Boris1']

isUserRegistrated=''
a=False

while isUserRegistrated not in ['y','n','Y','N']:
	isUserRegistrated=input('Добро пожаловать! Если вы уже зарегистрированы?(y/n): ')
if isUserRegistrated in ['N','n']:
	while a==False:
		newUser=input('Придумайте себе имя пользователя не длинне 12 символов: ')
		if isUserUnic(usernames,newUser)==False:
			print('Такой пользователь уже существует')	
print(newUser)

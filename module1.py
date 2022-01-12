import random
def isUserUnic(usernamesList:list,newUsername:str):
	"""
	:param usernamesList list: список всех пользователей
	:param newUsername str: имя пользователя введёное при регистрации
	:rtype bool:
	"""
	for i in range (len(usernamesList)):
		if usernamesList[i]==newUsername:
			isUnic=False
			return isUnic
			break
	isUnic=True
	return isUnic

def autoPassGenerator():
	"""
	:rtype char:
	"""
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper()
	str4 = str0+str1+str2+str3
	ls = list(str4)
	random.shuffle(ls)
	psword = ''.join([random.choice(ls) for x in range(12)])
	return psword

def isPassOkay(password:str):
	passOk=True
	"""
	:password str: пароль придуманный пользователем
	:rtype bool:
	"""
	str0 = ".,:;!_*-+()/#¤%&"
	alpha=digit=upper=special=0
	ls = list(str0)
	psword = list(password)
	for i in range(len(psword)):
		if psword[i].isupper():
			upper=1
		if psword[i].isalpha():
			alpha=1
		if psword[i].isdigit():
			digit=1
		if psword[i] in ls:
			special=1
	if alpha==1 and digit==1 and upper==1 and special==1 and len(psword)>7:
		passOk=True
	else:
		passOk=False
	return passOk

def isUserCorrect(username, password, userList, passList):
	"""
	:username char: логин пользователя
	:password char: пароль пользователя
	:userList list: список пользователей
	:passList list: список паролей
	:rtype bool:
	"""
	if username in userList and password in passList and userList.index(username)==passList.index(password):
		return True
	else:
		if username in [userList]==True:
			print('User OK')
		if password in [passList]==True:
			print('Pass OK')
		if userList.index(username)==passList.index(password):
			print('Index OK')
		return False
def whileYes(answers:list,question:str,):
	inputUser=''
	"""
	:answers list: варианты ответов
	:question str: вопрос
	:rtype bool:
	"""
	while inputUser not in answers:
		inputUser=input(question)
		if inputUser not in answers:
			print('Данного варианта ответа не существует')
	return True

def RpC(choice:str):
	"""
	:choice str: что выбирает игрок
	:rType str:
	"""
	itemsList=['камень','ножницы','бумага']
	bot=random(0,3)
	if bot==itemsList.index(choice):
		otvet=f'{itemsList[bot]} против {choice} - Ничья'
	elif bot==0 and choice=='ножницы' or bot==1 and choice=='бумага' or bot==2 and choice=='камень':
		otvet=f'{itemsList[bot]} против {choice} - Бот победил'
	elif bot==0 and choice=='бумага' or bot==1 and choice=='камень' or bot==2 and choice=='ножницы':
		otvet=f'{itemsList[bot]} против {choice} - Бот победил'
	return otvet

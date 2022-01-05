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
			print('upper', upper)
		if psword[i].isalpha():
			alpha=1
			print('alpha', alpha)
		if psword[i].isdigit():
			digit=1
			print('digit', digit)
		if psword[i] in ls:
			special=1
			print('spe', special)
	if alpha==1 and digit==1 and upper==1 and special==1:
		passOk=True
		print('Tr')
	else:
		passOk=False
		print('Fa')
	return passOk
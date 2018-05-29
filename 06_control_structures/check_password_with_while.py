# -*- coding: utf-8 -*-
#!/usr/bin/python3

username = input('Введите имя пользователя: ' )
password = input('Введите пароль: ' )

while True:
	if len(password) < 8:
		print('Пароль слишком короткий\n')
	elif username in password:
		print('Пароль содержит имя пользователя\n')
	else:
		print('Пароль для пользователя {} установлен'.format( username ))
		break		
	password = input('Введите пароль еще раз: ' )


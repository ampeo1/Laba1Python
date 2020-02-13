#!/usr/bin/env python

str = input('Введите текст: ')

list = str.split(' ')
#Разбиваем текст на слова
dictionary = {}


for index in range(0, len(list)):
	str = list[index]

	if str == '':
		continue
	#Если вводят несколько пробелов, то появляется мусор

	if str[len(str) - 1] == ',' or str[len(str) - 1] == '.':
		str = str[0: len(str) - 1]
	#Избавляемся от запятых и точек в словах
		
	if dictionary.get(str) == None:
		dictionary[str] = 1
	#если слово встречается впервый раз, то присваевываем 1
	else:
		dictionary[str] = dictionary[str] + 1

	print(dictionary)

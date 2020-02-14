#!/usr/bin/env python3

str = input('Введите текст: ')
str.lower()

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

#2 Задание
topWords = sorted(dictionary.items(), key = lambda count: count[1])
#Сортируем элементы по значению
#Нельзя перевернуть с помощью reverse(), т к кортеж - неизменяемый список

str = ''
#отделяем клю(слово) от кортежа и закидываем с строку
for index in range(len(topWords) - 1, len(topWords) - 11, -1):
	word = topWords[index]
	str = str + ' ' + word[0]
print(str + '.')

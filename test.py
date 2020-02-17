#!/usr/bin/env python3
#./test.py

import sys
import argparse

def wordCount(str):
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
	print(dictionary)
#2 Задание
	topWords = sorted(dictionary.items(), key = lambda count: count[1])
#Сортируем элементы по значению
#Нельзя перевернуть с помощью reverse(), т к кортеж - неизменяемый список

	str = ''
	counter = 0
#отделяем клю(слово) от кортежа и закидываем с строку
	for index in range(len(topWords) - 1, -1, -1):
		if counter == 10:
			break
		word = topWords[index]
		str = str + ' ' + word[0]
		counter = counter + 1
	print(str + '.')


def quickSort (list, leftRange, rightRange):
	if rightRange - leftRange < 2:
		return 
	for index in range(rightRange - 1, leftRange, -1):
		if list[index]  < list[index - 1]:
			list[index], list[index - 1] = list[index - 1], list[index]
		else:
			quickSort(list, index, rightRange)
			quickSort(list, leftRange, index)
	quickSort(list, index, rightRange)
	quickSort(list, leftRange, index)	


def merg(list, leftRange, mid, rightRange):
	indexLeft = leftRange
	indexRight = mid
	buffer = []
	while indexLeft < mid and indexRight < rightRange:
		if list[indexLeft] < list[indexRight]:
			buffer.append(list[indexLeft])
			indexLeft = indexLeft + 1
		else:
			buffer.append(list[indexRight])
			indexRight = indexRight + 1
	if(indexLeft < mid):
		buffer.extend(list[indexLeft: mid])
	elif(indexRight < rightRange):
		buffer.extend(list[indexRight: rightRange])
	list[leftRange: rightRange] = buffer


def mergSort(list, leftRange, rightRange):
	if leftRange + 1 >= rightRange:
		return
	mid = int((leftRange + rightRange) / 2)
	mergSort(list, leftRange, mid)
	mergSort(list, mid, rightRange)
	merg(list, leftRange, mid, rightRange)


def fib(n):
	n = int(n)
		
	cache = [1, 1]

	print(cache[0])
	print(cache[1])

	for index in range(2, n):
		cache[1] = cache[0] + cache[1]
		cache[0] = cache[1] - cache[0]
		print(cache[1])


def createParse():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', default = 'input')
	parser.add_argument('-t', '--task', choices = ['task1', 'task2', 'task3', 'task4'], default = 'task1')

	return parser



parser = createParse()
namespace = parser.parse_args(sys.argv[1:])

str = ''
with open(namespace.file) as file:
	for line in file:
		str = str + line

if(namespace.task == 'task1'):
	wordCount(str)	
elif(namespace.task == 'task2'):
	list = [int(x) for x in str.split(' ')]
	quickSort(list, 0, len(str.split(' ')))
	print(list)
elif(namespace.task == 'task3'):
	list = [int(x) for x in str.split(' ')]
	mergSort(list, 0, len(str.split(' ')))
	print(list)
elif(namespace.task == 'task4'):
	fib(str)
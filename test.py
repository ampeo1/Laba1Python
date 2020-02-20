#!/usr/bin/env python3
#./test.py

import sys
import argparse
import random
import pdb

def word_count(str):
	str.lower()

	words = str.split(' ')
#Разбиваем текст на слова
	dictionary = {}

	for index in range(0, len(words)):
		str = words[index]

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
	words = sorted(dictionary.items(), key = lambda count: count[1])
#Сортируем элементы по значению
#Нельзя перевернуть с помощью reverse(), т к кортеж - неизменяемый список

	dictionary = dict(words[-10:])
	words = list(dictionary.keys())
	print(' '.join(words))


def quick_sort(list):
	if len(list) < 2:
		return
	sup_elem = random.choice(list)
	less = []
	more = []
	equals = []
	for elem in list:
		if elem < sup_elem:
			less.append(elem)
		elif elem > sup_elem:
			less.append(elem)
		elif elem == sup_elem:
			equals.append(elem)
	return quick_sort(less) + equals + quick_sort(more)

def merg(list, left_range, mid, right_range):
	index_left = left_range
	index_right = mid
	buffer = []
	while index_left < mid and index_right < right_range:
		if list[index_left] < list[index_right]:
			buffer.append(list[index_left])
			index_left = index_left + 1
		else:
			buffer.append(list[index_right])
			index_right = index_right + 1
	if(index_left < mid):
		buffer.extend(list[index_left: mid])
	elif(index_right < right_range):
		buffer.extend(list[index_right: right_range])
	list[left_range: right_range] = buffer


def merg_sort(list, left_range, right_range):
	if left_range + 1 >= right_range:
		return
	mid = int((left_range + right_range) / 2)
	merg_sort(list, left_range, mid)
	merg_sort(list, mid, right_range)
	merg(list, left_range, mid, right_range)


def fib(n):
	n = int(n)
		
	cache = [1, 1]

	print(cache[0])
	print(cache[1])

	for index in range(2, n):
		cache[1] = cache[0] + cache[1]
		cache[0] = cache[1] - cache[0]
		print(cache[1])


def create_parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', default = 'input')
	parser.add_argument('-t', '--task', choices = ['task1', 'task2', 'task3', 'task4'], default = 'task1')

	return parser



parser = create_parse()
namespace = parser.parse_args(sys.argv[1:])

str = ''
with open(namespace.file) as file:
	for line in file:
		str = str + line

if(namespace.task == 'task1'):
	word_count(str)	
elif(namespace.task == 'task2'):
	list = [int(x) for x in str.split(' ')]
	quick_sort(list)
	print(list)
elif(namespace.task == 'task3'):
	list = [int(x) for x in str.split(' ')]
	merg_sort(list, 0, len(str.split(' ')))
	print(list)
elif(namespace.task == 'task4'):
	fib(str)
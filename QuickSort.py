#!/usr/bin/env python3
import pdb
def QuickSort (list, leftRange, rightRange):
	pdb.set_trace()
	if rightRange - leftRange < 2:
		return 
	for index in range(rightRange - 1, leftRange, -1):
		if list[index]  < list[index - 1]:
			list[index], list[index - 1] = list[index - 1], list[index]
		else:
			QuickSort(list, index, rightRange)
			QuickSort(list, leftRange, index)
	QuickSort(list, index, rightRange)
	QuickSort(list, leftRange, index)	

str = input("Введите числа: ")
list = [int(x) for x in str.split(' ')]
QuickSort(list, 0, len(str.split(' ')))
print(list)


#!/usr/bin/env python3
#./MergeSort.py
import pdb

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

str = ''
with open('input') as file:
	for line in file:
		str = str + line

list = [int(x) for x in str.split(' ')]
mergSort(list, 0, len(str.split(' ')))
print(list)
#!/usr/bin/env python3
#./Fibonachi.py

with open('input') as file:
	for line in file:
		n = int(line)
		
cache = [1, 1]

print(cache[0])
print(cache[1])

for index in range(2, n):
	cache[1] = cache[0] + cache[1]
	cache[0] = cache[1] - cache[0]
	print(cache[1])
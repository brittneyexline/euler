#!/usr/local/bin/python
#coding: utf8
import math

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

LIMIT = 3724680960
divisors = [ 20, 19, 18, 17, 16, 14, 13, 11]
x = 2520

while (x < LIMIT):
	divides = True
	for d in divisors:
		if (x % d != 0):
			divides = False
			break
	if (divides):
		print x
		break
	x += 20

#!/usr/local/bin/python
#coding: utf8
import math

# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

fibonacci_cache = {}

def fibonacci (n):
	if (n < 1):
		return 0
	elif (n == 1):
		return 1
	elif (n == 2):
		return 2
	elif (n in fibonacci_cache):
		return fibonacci_cache[n]
	else:
		r = fibonacci(n-1) + fibonacci(n-2)
		fibonacci_cache[n] = r
		return r

term = 0
index = 1

while (len(str(term)) < 1000):
	term = fibonacci(index)
	index += 1

print 'index: ' + str(index) + ', term: ' + str(term)
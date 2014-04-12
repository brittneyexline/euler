#!/usr/local/bin/python
#coding: utf8
import math

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

MAX_START = 1000000
collatz_cache = {}

def collatz (n):
	if (n == 1):
		return 1
	elif n in collatz_cache:
		return collatz_cache[n]
	elif (n % 2 == 0):
		c = collatz(n/2)
		collatz_cache[n] = 1 + c
		return 1 + c
	else:
		c = collatz(3*n + 1)
		collatz_cache[n] = 1 + c
		return 1 + c

max_chain = 0
term = 0

for x in range(13, MAX_START):
	c = collatz(x)
	print str(x) + ': ' + str(c)
	if (c > max_chain):
		max_chain = c
		term = x

print 'MAX CHAIN: ' + str(max_chain)
print 'TERM: ' + str(term)
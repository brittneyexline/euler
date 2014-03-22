#!/usr/local/bin/python
#coding: utf8
import math

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome (s):
	if (s == s[::-1]):
		return True
	else:
		return False

p = 0
for i in reversed(range(100, 999)):
	for j in reversed(range(100, i)):
		m = i*j
		if (is_palindrome(str(m)) and m > p):
			p = m
			break

print p
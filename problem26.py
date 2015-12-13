#!/usr/local/bin/python
#coding: utf8
import math
import re
from decimal import *

# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the
# longest recurring cycle in its decimal fraction part.

getcontext().prec = 5000
longest_substring_ever = ''
x_with_longest_substring = 0
for x in range(2, 1000):
	print 'Calculating substring for x = ' + str(x)
	decimal_string = str(Decimal(1) / Decimal(x))
	decimal_string = decimal_string[2:]
	print decimal_string
	longest_substring = '';
	current_substring = '';
	for i in range(3, (len(decimal_string)-1)/3):
		for j in range(i, (len(decimal_string)-1)/3):
			current_substring = decimal_string[i:j+1]
			# print str(i) + ', ' + str(j) + ': ' + current_substring
			if (re.search(current_substring, decimal_string[j+1:]) and len(current_substring) > len(longest_substring)):
				if (current_substring == decimal_string[j+1:j+1+j+1-i] and current_substring == decimal_string[j+1+j+1-i:j+1+j+1-i+j+1-i]):
					longest_substring = current_substring
					break
			else:
				break
	if (longest_substring == ''):
		print '!!!!!!!!OMG!!!!!!!! no longest substring found for ' + str(x)
	print 'longest substring: ' + str(longest_substring)
	if (len(longest_substring) > len(longest_substring_ever)):
		longest_substring_ever = longest_substring
		x_with_longest_substring = x
print 'x = ' + str(x_with_longest_substring) + ' has longest substring: ' + longest_substring_ever

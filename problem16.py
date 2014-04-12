#!/usr/local/bin/python
#coding: utf8
import math

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

x = int(math.pow(2, 1000))
sum = 0
print x
for c in str(x):
	sum += int(c)

print sum
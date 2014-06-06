#!/usr/local/bin/python
#coding: utf8
import math

# A perfect number is a number for which the sum of its proper divisors is exactly
# equal to the number. For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit cannot be
# reduced any further by analysis even though it is known that the greatest number that
# cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written
# as the sum of two abundant numbers.

abundant_cache = {}
not_abundant_cache = {}
ABUNDANT_LIMIT = 28123

def find_factors (n):
	factors = [1]
	for i in range(2, int(math.sqrt(n) + 1)):
		if (n % i == 0):
			factors.append(i)
			if (n/i != i):
				factors.append(n/i)
	return factors

def is_abundant (n):
	if n in abundant_cache:
		return True
	elif n in not_abundant_cache:
		return False
	f = find_factors(n)
	s = sum(f)
	if s > n:
		abundant_cache[n] = 1
		print str(n) + ' is abundant!'
		return True
	else:
		not_abundant_cache[n] = 1
		return False

def is_sum_abundant (n):
	for a in sorted(abundant_cache.keys()):
		if a >= n:
			return False
		elif is_abundant(n-a):
			return True
	return False

sum_abundant = 0
for n in range(1, ABUNDANT_LIMIT+1):
	is_abundant(n)
	if (not is_sum_abundant(n)):
		print str(n) + ' is not sum abundant!'
		sum_abundant += n

print sum_abundant
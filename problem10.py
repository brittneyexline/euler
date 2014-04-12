#!/usr/local/bin/python
#coding: utf8
import math

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

MAX_PRIME = 2000000
prime_cache = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1}
prime_index = 8
not_prime_cache = {1:1}

def is_prime (i):
	if (i in prime_cache):
		return True;
	elif (i in not_prime_cache):
		return False
	for x in range(2, int(math.sqrt(i))+1):
		if (not is_prime(x)):
			continue
		elif (i % x == 0):
			if (i < int(math.sqrt(MAX_PRIME))):
				not_prime_cache[i] = 1
			return False
	if (i < int(math.sqrt(MAX_PRIME))):
		prime_cache[i] = 1
	return True

total = 0
i = MAX_PRIME - 1

while (i > 1):
	if (is_prime(i)):
		total += i
	i -= 2

print total + 2
	
		
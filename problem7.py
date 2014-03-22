#!/usr/local/bin/python
#coding: utf8
import math

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

MAX_INDEX = 10001
prime_cache = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1}
largest_prime = 19
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
			not_prime_cache[i] = 1
			return False
	prime_cache[i] = 1
	return True

def next_prime (n):
	while (not is_prime(n)):
		n += 2
	return n

while (prime_index < MAX_INDEX):
	print str(prime_index) + ' : ' + str(largest_prime)
	largest_prime = next_prime(largest_prime+2)
	prime_index += 1

print largest_prime

#!/usr/local/bin/python
import math
import pprint

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

NUMBER = 600851475143
s = int(math.sqrt(NUMBER))

prime_cache = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1}
not_prime_cache = {1:1}

def is_prime (i):
	if (i in prime_cache):
		return True;
	elif (i in not_prime_cache):
		return False
	for x in range(2, int(math.sqrt(i))):
		if (not is_prime(x)):
			continue
		elif (i % x == 0):
			not_prime_cache[i] = 1
			return False
	prime_cache[i] = 1
	return True


while (s > 0):
	if (is_prime(s) and NUMBER % s == 0):
		print s
		break;
	s -= 1

#pprint.pprint(prime_cache)
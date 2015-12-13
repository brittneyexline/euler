#!/usr/local/bin/python
#coding: utf8

import math

# Euler discovered the remarkable quadratic formula:
# n² + n + 41
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
# The incredible formula  n² − 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values n = 0 to 79.
# The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
# n² + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

MAX_PRIME = 2000000
prime_cache = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1}
prime_index = 8
not_prime_cache = {1:1}

def is_prime (i):
	i = int(math.fabs(i))
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

def quadratic_formula(a, b, n):
	return n*n + a*n + b

a_with_max_prime = 0
b_with_max_prime = 0
max_num_primes = 0

for a in xrange(-1000, 1000):
	for b in xrange(-1000, 1000):
		result_is_prime = True
		n = 0
		while result_is_prime:
			result = quadratic_formula(a, b, n)
			if (not is_prime(result)):
				result_is_prime = False
				break
			n += 1
		if (n > max_num_primes):
			max_num_primes = n
			a_with_max_prime = a
			b_with_max_prime = b

print 'a = ' + str(a_with_max_prime) + ', b = ' + str(b_with_max_prime) + ' has most consecutive primes (' + str(max_num_primes) + ')'

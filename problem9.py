#!/usr/local/bin/python
#coding: utf8
import math

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def check_pythagorean(trip):
	if (trip[0]**2 + trip[1]**2 == trip[2]**2):
		return True
	else:
		return False

triplets = []

for a in range(1, 334):
	for b in range(2*a, 667):
		triplets.append((a, b-a, 1000-b))

for t in triplets:
	if (check_pythagorean(t)):
		print t
		print t[0] * t[1] * t[2]
		break

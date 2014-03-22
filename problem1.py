#!/usr/local/bin/python

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
current_multiple = 3

while (current_multiple < 1000):
	sum += current_multiple
	current_multiple += 3
	print current_multiple

current_multiple = 5

while (current_multiple < 1000):
	if (current_multiple % 3 == 0):
		current_multiple += 5
		continue
	else:
		sum += current_multiple
	current_multiple += 5
	print current_multiple

print sum
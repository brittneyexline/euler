#!/usr/local/bin/python
#coding: utf8

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

spiral_sizes = [2*x for x in range(1, 501)]
diagonal_number_sum = 1
current_diagonal_number = 1

for x in spiral_sizes:
	for y in range(4):
		current_diagonal_number += x
		diagonal_number_sum += current_diagonal_number

print str(diagonal_number_sum)

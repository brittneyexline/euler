#!/usr/local/bin/python
#coding: utf8
import math

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right
# and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

def flip (path):
	flipped = ''
	for c in path:
		if (c == '1'):
			flipped += '0'
		elif (c == '0'):
			flipped += '1'
	return flipped

def next_lattice_paths (paths, c):
	new_paths = {}
	for p in paths:
		if (c == '0'):
			for x in range(0, len(p)/2+1):
				np = p[:x] + c + p[x:]
				new_paths[np] = 1
				new_paths[np[::-1]] = 1
		else:
			np = p + c
			new_paths[np] = 1
			new_paths[flip(np)] = 1
	return new_paths.keys()

def calculate_lattice_paths (steps):
	if (steps == 1):
		return 1
	half = int(steps/2)
	if (steps % 2 != 0):
		half += 1
	return steps * calculate_lattice_paths(steps -1) / half

#current_paths = ['01','10']
#for x in range(2, 21):
#	current_paths = next_lattice_paths(current_paths, '0')
#	print str(x-1) + '.5: ' + str(len(current_paths))
#	current_paths = next_lattice_paths(current_paths, '1')
#	print str(x) + ': ' + str(len(current_paths))

print calculate_lattice_paths(40)
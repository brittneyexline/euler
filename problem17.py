#!/usr/local/bin/python
#coding: utf8
import math

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

ones_place = {
	0 : '',
	1 : 'one',
	2 : 'two',
	3 : 'three',
	4 : 'four',
	5 : 'five',
	6 : 'six',
	7 : 'seven',
	8 : 'eight',
	9 : 'nine',
}

teens = {
	10 : 'ten',
	11 : 'eleven',
	12 : 'twelve',
	13 : 'thirteen',
	14 : 'fourteen',
	15 : 'fifteen',
	16 : 'sixteen',
	17 : 'seventeen',
	18 : 'eighteen',
	19 : 'nineteen',
}

tens_place = {
	2 : 'twenty',
	3 : 'thirty',
	4 : 'forty',
	5 : 'fifty',
	6 : 'sixty',
	7 : 'seventy',
	8 : 'eighty',
	9 : 'ninety',
}

def int_to_word (n):
	if (len(n) == 1):
		return ones_place[int(n)]
	elif (len(n) == 2):
		if (n[0] == '1'):
			return teens[int(n)]
		elif (n[0] == '0'):
			return int_to_word(n[1])
		else:
			return tens_place[int(n[0])] + ones_place[int(n[1])]
	elif (len(n) == 3):
		if (n[1:] == '00'):
			return ones_place[int(n[0])] + 'hundred'
		else:
			return ones_place[int(n[0])] + 'hundredand' + int_to_word(n[1:])
	elif (len(n) == 4 and n == '1000'):
		return 'onethousand'
	else:
		return ''

all = ''
for x in range (1, 1001):
	word = int_to_word(str(x))
	print word
	all += word

print len(all)
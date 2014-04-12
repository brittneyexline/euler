#!/usr/local/bin/python
#coding: utf8
import math

# You are given the following information,
# but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

day = 1
year = 1900

num_first_sundays = 0

while (year <= 2000):
	month = 1
	while (month <= 12):
		if (month != 2 or (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))):
			day = (day+days_in_month[month]) % 7
		else:
			day = (day+29) % 7
		if (day == 0):
			print str(month) + ' ' + str(year)
			num_first_sundays += 1
		month += 1
	year += 1

print num_first_sundays
	
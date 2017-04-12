#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split("\t") # delimit input by tab 
    if len(data) == 5: # if length of data equal to 5
        store, dept, date, sales, holidays = data  # assign each entry to a variable
        print "{0}\t{1}\t{2}".format(store, sales, holidays) #delimits printed output by tab

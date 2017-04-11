#!/usr/bin/python

 # Format of each line is:
 # date\ttime\tstore name\titem description\tcost\tmethod of payment
 #
 # We want elements 2 (store name) and 4 (cost)
 # We need to write them out to standard output, separated by a tab

 import sys

 for line in sys.stdin:
     data = line.strip().split("\t")
     if len(data) == 5:
         store, dept, date, sales, holidays = data
         print "{0}\t{1}\t{2}".format(store, sales, holidays
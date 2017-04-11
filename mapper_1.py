from __future__ import division
from itertools import groupby
import itertools
#import groupby
import operator


f = open("train.txt","r")  # open file, read-only raw data

o = open("o.txt", "w") # open file, write - just our key, value pairs

for line in f:  

    data = line.strip().split("\t") 

    #print data

    #print len(data)

    if len(data) == 5:

        store, dept, date, sales, holidays = data

        print "{0}\t{1}\t{2}".format(store, sales, holidays)

       
f.close()
o.close()

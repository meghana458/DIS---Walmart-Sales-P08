#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
#import operator
#import itertools
sorted = open("o.txt","r")   
results = open("results2.txt", "w")   

salesTotal = 0        
oldStore = None
lines = sorted.readlines()
for line in lines:
    datalist = line.strip().split("\t")
	#print len(datalist)
	
    if len(datalist) != 3:  # if bad input line
       continue             # ignore it

    thisStore, thisSale, thisHolidays = datalist  # read into variables

    if oldStore and oldStore != thisStore:        
        results.write("{0}\t{1}\n".format(oldStore, salesTotal))
        oldStore = thisStore;
        salesTotal = 0
    else:
	    if thisHolidays == "FALSE":
               oldStore = thisStore            
               salesTotal += float(thisSale)
if oldStore != None: 
    results.write("{0}\t{1}\n".format(oldStore, salesTotal))

sorted.close() 
results.close()
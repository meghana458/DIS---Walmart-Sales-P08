#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
#import operator
#import itertools
#o = open("o.txt","w")
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale, thisHolidays = data_mapped

    if oldKey and (oldKey != thisKey):
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0
    else:
        if thisHolidays == "FALSE":
                oldKey = thisKey
                salesTotal += float(thisSale)
                #print salesTotal, "\t", oldKey, "\t", thisHolidays
if oldKey != None:
    print salesTotal, "\t", oldKey, "\t", thisHolidays
    #o.write("{1}\t{0}\n".format(salesTotal,oldKey)

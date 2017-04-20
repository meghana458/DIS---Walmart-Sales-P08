f = open("train2.txt","r")  # open file, read-only raw data
o = open("o.txt", "w") # open file, write - just our key, value pairs
for line in f:  
    data = line.strip().split("\t") 
    #print data
    #print len(data)
    if len(data) == 5:
        store, dept, date, sales, holidays = data
        #print "{0}\t{1}\t{2}".format(store, sales, holidays)
        o.write("{0}\t{1}\t{2}\n".format(store, sales, holidays))
f.close()
o.close()
import csv
import operator
File = open("/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv", "r")
csvfile = csv.reader(File,delimiter=',')
sort = sorted(csvfile,key=operator.itemgetter(1))
for eachline in sort:
        print eachline
print "The date of the highest water level is:", eachline




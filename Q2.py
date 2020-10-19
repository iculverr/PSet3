import csv
import operator
File = open("/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv", "r")
csvfile = csv.reader(File,delimiter=',')
sort = sorted(csvfile,key=operator.itemgetter(1))
#Operator gives value to each csv column. 0 is the first element, 1 is the second element etc
for eachline in sort:
        print eachline
sortb = sorted(csvfile,key=operator.itemgetter(1),reverse=True)
for eachlineb in sortb:
	print eachlineb
print "The date of the highest water level is:", eachline
print "The date of the lowest water level is:", eachlineb
print "The date of the highest water level is:", eachline







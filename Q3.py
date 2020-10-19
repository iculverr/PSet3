import csv
import operator
File = open("/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv", "r")
csvfile = csv.reader(File,delimiter=',')
sort = sorted(csvfile,key=operator.itemgetter(1))
a = sort.split(',')[1]
isitgreater=[]
line_num = 0
#Attempt at sorting specifically the water level column then finding the difference 
#and adding it to a list if the difference is greater than the previous one.
for eachline in sort:
        line_num += 1
        b = sort.split(',')[1]
        Difference = b-a
        if Difference > isitgreater
          isitgreater.append(Difference)
        else
          continue
print "The the highest water level change is:", Difference "Line number for date is:", line_num
#It's supposed to find the number that matches the difference but
#that clearly won't work cuz the difference wouldn't even be in the csv file
#I don't know how to pair the difference variable to line number :(
import re
for eachline in sort:
  x = re.findall(d*\.\d*)
  if x = Difference
    print(eachline)
    break
  else
    continue
    



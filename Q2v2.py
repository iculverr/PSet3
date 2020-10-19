File = open("/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv", "r")
waterlevel = [0]
#Tried to get one column out of linesplit, wouldve been easier to just do a !cut command prob
for eachline in File:
  eachline.split(',')[1]
  #Can't for the life of me figure out how to set an array value for the split elements
  waterlevel.append()
avg = sum(waterlevel)/len(waterlevel)
print(avg)

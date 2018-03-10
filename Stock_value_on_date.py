import csv
import pandas

# Can add volume and name as well
colnames= ['Date','Open','High','Low','Close']

data = pandas.read_csv('AMD_data.csv',names=colnames)

date = data.Date.toList()
print (data)

# with open('AMD_data.csv',newline='')as csvfile:
#     spamreader = csv.reader(csvfile,delimiter =' ',quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
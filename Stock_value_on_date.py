import csv
from api_newspaper_test import articleList

#Hola, thank you for checking out the code. What you're looking for is probably
#datesAndValues.. right now the range of what we're getting isn't pretty wide,
#so if you want more data, just set the range wider in api_newspaper_test.py


#for csv data
#downloaded from https://www.nasdaq.com/symbol/amd/historical]
newsAPIdates = []
datesAndValues = [] 

#stores targeted dates along with the corresponding high and low (using newsAPI and AMD_data.csv)
class Information:
    informationCount = 0

#can also get other values, refer to AMD_data.csv
    def __init__(self,date,high,low):
        self.date = date
        self.dayhigh = high
        self.daylow = low
        self.informationCount += 1

    def __repr__(self):
        return "< " + str(self.informationCount) +"; date = " + str(self.date) + "; high = " + str(self.dayhigh) + "; low = " + str(self.daylow) + ">"           

#data returned from newsAPI doesn't match the format from AMD_data.csv, this corrects that
def dateManipulation( someArticle ):

    dateOfArticle = someArticle.date
    pureDate = dateOfArticle.split('T', 1)[0]
    matchingDate = pureDate.replace ("-","/")

    newsAPIdates.append(matchingDate)

for singleArticle in articleList:
    dateManipulation(singleArticle)

#fetching the right AMD_data value for the newsAPI target date
def newsAPIandCSVcompare (csv):
    for newsAPIdate in newsAPIdates:
        if csv[0] == newsAPIdate:
            registeredInfo = Information(csv[0],csv[4],csv[5])
            datesAndValues.append(registeredInfo)      

#reading AMD_data file
with open(r'AMD_data.csv')as f:
    reader=csv.reader(f)
    for row in reader:
        if row:
            newsAPIandCSVcompare(row)

#check it out, it works
print(datesAndValues)

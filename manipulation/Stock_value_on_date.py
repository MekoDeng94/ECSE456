import csv
import json
from runner.console_monochrome import Console

logger = Console()
#for csv data
#downloaded from https://www.nasdaq.com/symbol/amd/historical]

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

    return matchingDate

#fetching the right AMD_data value for the newsAPI target date
def newsAPIandCSVcompare (csv, newsAPIdates):
    datesAndValues = []

    for newsAPIdate in newsAPIdates:
        logger.info('comparing: ' + csv[0] + ' to ' + newsAPIdate)
        if csv[0] == newsAPIdate:
            logger.info('matching dates: ' + str(newsAPIdate))
            registeredInfo = Information(csv[0],csv[4],csv[5])
            #TODO: format correctly
            return registeredInfo

    return datesAndValues    

def link_stock_value_to_article_date(article_list):
    complete_data = []
    newsAPIdates = []

    logger.info('manipulating article dates ...')
    for singleArticle in article_list:
        matchingDate = dateManipulation(singleArticle) 
        newsAPIdates.append(matchingDate) 

    #reading AMD_data file
    with open(r'AMD_data.csv')as f:
        logger.info('reading AMD_data.csv ...')
        reader=csv.reader(f)
        for row in reader:
            if row:
                compared_result = newsAPIandCSVcompare(row, newsAPIdates)
                #TODO: a little too recursive here
                if compared_result != []:
                    complete_data.append(compared_result)
    
    return complete_data

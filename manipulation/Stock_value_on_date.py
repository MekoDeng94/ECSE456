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
    def __init__(self,date,close_value,open_value,high,low,url,polarity,subjectivity):
        self.date = date
        self.close = close_value
        self.open = open_value
        self.dayhigh = high
        self.daylow = low
        self.url = url
        self.polarity = polarity
        self.subjectivity = subjectivity
        self.informationCount += 1

    def __repr__(self):
        return "< " + str(self.informationCount) +"; date = " + str(self.date) +"; close = " + str(self.close) +"; open = " + str(self.open)+ "; high = " + str(self.dayhigh) + "; low = " + str(self.daylow) + "; url = " + str(self.url) + "; polarity = " + str(self.polarity) + "; subjectivity = " + str(self.subjectivity) +">"           

class Information_vader:
    informationCount = 0

    # def __init__(self, date, open_value, close_value, high, low, volumne, compound):
    #     self.date = date
    #     self.open = open_value
    #     self.close = close_value
    #     self.dayhigh = high
    #     self.daylow = low
    #     self.compound = compound
    #     self.informationCount += 1

    # def __repr__(self):
    #     return "< " + str(self.informationCount) +"; date = " + str(self.date) +"; open = " + str(self.open) + "; high = " + str(self.dayhigh) + "; low = " + str(self.daylow) + "; url = " + str(self.url) + "; pos = " + str(self.pos) + "; neg = " + str(self.neg) + "; neu = " + str(self.neu) + "; compound = " + str(self.compound) + ">"             

#can also get other values, refer to AMD_data.csv
    def __init__(self,date,close_value,open_value,volume,high,low,url,pos,neg, neu, compound):
        self.date = date
        self.close = close_value
        self.open = open_value
        self.volume = volume
        self.dayhigh = high
        self.daylow = low
        self.url = url
        self.pos = pos
        self.neg = neg
        self.neu = neu
        self.compound = compound
        self.informationCount += 1

    def __repr__(self):
        return "< " + str(self.informationCount) +"; date = " + str(self.date) +"; close = " + str(self.close) + "; open = " + str(self.open) +"; volume = " + str(self.volume) + "; high = " + str(self.dayhigh) + "; low = " + str(self.daylow) + "; url = " + str(self.url) + "; pos = " + str(self.pos) + "; neg = " + str(self.neg) + "; neu = " + str(self.neu) + "; compound = " + str(self.compound) + ">"             

#data returned from newsAPI doesn't match the format from AMD_data.csv, this corrects that
def dateManipulation( someArticle ):
    dateOfArticle = someArticle.date
    pureDate = dateOfArticle.split('T', 1)[0]
    matchingDate = pureDate.replace ("-","/")

    someArticle.date = matchingDate

    return someArticle

#fetching the right AMD_data value for the newsAPI target date
def newsAPIandCSVcompare (csv, newsAPIdates_article):
    datesAndValues = []

    for article in newsAPIdates_article:
        logger.info('comparing: ' + csv[0] + ' to ' + article.date)
        if csv[0] == article.date:
            logger.info('matching dates: ' + str(article.date))
            registeredInfo = Information(csv[0],csv[3],csv[2],csv[4],csv[5],article.url, article.polarity, article.subjectivity)
            datesAndValues.append(registeredInfo)

    return datesAndValues

#fetching the right AMD_data value for the newsAPI target date
def newsAPIandCSVcompare_vader(csv, newsAPIdates_article):
    datesAndValues = []

    for article in newsAPIdates_article:
        logger.info('comparing: ' + csv[0] + ' to ' + article.date)
        if csv[0] == article.date:
            logger.info('matching dates: ' + str(article.date))
            registeredInfo = Information_vader(csv[0],csv[1],csv[3],csv[2],csv[4],csv[5],"NONE", 0, 0, 0, article.compound)
            datesAndValues.append(registeredInfo)

    return datesAndValues    

def link_stock_value_to_article_date(article_list, sentiment_tool):
    complete_data = []
    newsAPIdates_article = []

    logger.info('manipulating article dates ...')
    for singleArticle in article_list:
        matchingDate_Article = dateManipulation(singleArticle) 
        newsAPIdates_article.append(matchingDate_Article) 

    #reading AMD_data file
    with open(r'AMD_data.csv')as f:
        logger.info('reading AMD_data.csv ...')
        f.readline()
        reader=csv.reader(f)
        for row in reader:
            if row:
                if (sentiment_tool == 'textblob'):
                    compared_result = newsAPIandCSVcompare(row, newsAPIdates_article)
                if (sentiment_tool =='vader'):
                    compared_result = newsAPIandCSVcompare_vader(row, newsAPIdates_article)

                logger.info(compared_result)
                if compared_result != []:
                    complete_data.append(compared_result)
    
    return complete_data

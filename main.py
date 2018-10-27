# from manipulation.newsAPI_manipulation import anArticle
import argparse
import datetime
import csv
from newsapi import NewsApiClient
from manipulation.newsAPI_manipulation import get_updated_articles, create_articleList, clean_articleList,anArticle
#from manipulation.newsAPI_manipulation_vader import get_updated_articles_vader, create_articleList_vader, anArticle_vader
from manipulation.Stock_value_on_date import link_stock_value_to_article_date
from runner.console_monochrome import Console

parser = argparse.ArgumentParser(description='So far, collecting data for stock market prediction')
parser.add_argument('--create-csv', dest='createCSV', help='scraping articles from most recent date and applying stock market values on that day', action='store_true')
parser.add_argument('--sentiment-tool', dest='sentimentTool', help='specify the sentiment analysis tool: "vader" or "textblob"', action='store')
args = parser.parse_args()

CREATECSV = args.createCSV
sentiment_tool = args.sentimentTool

logger = Console()
now = datetime.datetime.now()

#update 13/09/18: news api only goes back a month. TABARNAK
from_date = ''
to_date = ''

# sentiment_tool = 'vader'

def date_formatter():
    dates = {'start':'', 'end':''}

    start_month = "{num:0>2}".format(num=(now.month-1))
    end_month = "{num:0>2}".format(num=now.month)
    day = "{num:0>2}".format(num=now.day)
    
    start_date = str(now.year) + '-' + str(start_month) + '-' + str(day)
    end_date = str(now.year) + '-' + str(end_month) + '-' + str(day)
    
    dates['start'] = start_date
    dates['end'] = end_date

    return dates

if CREATECSV:
    dates_range = date_formatter()
 
    from_date = '2018-08-14'
    to_date = '2018-08-20'

    # from_date = dates_range['start']
    # to_date = dates_range['end']

    #TODO: transfer the returned data (useful_data) to a csv file and continue from the last registered date
    article_list = create_articleList(from_date,to_date, sentiment_tool)
    article_list_compound = clean_articleList(article_list)
    useful_data = link_stock_value_to_article_date(article_list_compound, sentiment_tool)   

    if (sentiment_tool == 'textblob'):
        csv = open('manipulated_data_textblob.csv',"w")
        columnTitleRow_textblob = "date, url, open_value, high, low, polarity, subjectivity\n"
        csv.write(columnTitleRow_textblob)

        for data in useful_data:
            for i in data:
                open_value = i.open
                date = i.date
                url = i.url
                high = i.dayhigh
                low = i.daylow
                polarity = i.polarity
                subjectivity = i.subjectivity   
                row = str(date) + "," + str(url) + ',' + str(open_value) + ',' + str(high) + ',' + str(low) + ',' + str(polarity) + ',' + str(subjectivity) + '\n'
                        
                csv.write(row)

    if (sentiment_tool =='vader'):
        csv = open('manipulated_data_vader.csv',"w")
        columnTitleRow_vader = "date, open_value, close_value, volume, high, low, compound\n"
        csv.write(columnTitleRow_vader)

        for data in useful_data:
            for i in data:
                close_value = i.close
                volume = i.volume
                open_value = i.open
                date = i.date
                high = i.dayhigh
                low = i.daylow
                compound = i.compound
                row = str(date) + ',' + str(open_value) + ',' + str(close_value) + ',' + str(volume) + ',' + str(high) + ',' + str(low) + ',' + str(compound) + '\n'
                        
                csv.write(row)


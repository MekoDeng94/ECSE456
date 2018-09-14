# from manipulation.newsAPI_manipulation import anArticle
import argparse
import datetime
import csv
from newsapi import NewsApiClient
from manipulation.newsAPI_manipulation import get_updated_articles, create_articleList, anArticle
from manipulation.newsAPI_manipulation_vader import get_updated_articles_vader, create_articleList_vader, anArticle_vader
from manipulation.Stock_value_on_date import link_stock_value_to_article_date
from runner.console_monochrome import Console

parser = argparse.ArgumentParser(description='So far, collecting data for stock market prediction')
parser.add_argument('--create-csv', dest='createCSV', help='scraping articles from most recent date and applying stock market values on that day', action='store_true')
args = parser.parse_args()

CREATECSV = args.createCSV

logger = Console()
now = datetime.datetime.now()

#update 13/09/18: news api only goes back a month. TABARNAK
from_date = ''
to_date = ''


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

    # from_date = dates_range['start']
    from_date = '2018-09-11'
    to_date = '2018-09-11'
    # to_date = dates_range['end']

    #TODO: transfer the returned data (useful_data) to a csv file and continue from the last registered date
    article_list = create_articleList_vader(from_date, to_date)

    #all useful dates (TODO: add sentiment analysis to the returned result)
    # article_list = [anArticle('sss','d','2018/09/12','0','0'),anArticle('sff','d','2018/09/12','0','0')]
    useful_data = link_stock_value_to_article_date(article_list)

    exit()
    csv = open('manipulated_data.csv',"w")

    columnTitleRow = "date, url, high, low, polarity, subjectivity\n"
    csv.write(columnTitleRow)

    for data in useful_data:
        for i in data:
            date = i.date
            url = i.url
            high = i.dayhigh
            low = i.daylow
            polarity = i.polarity
            subjectivity = i.subjectivity
            row = str(date) + "," + str(url) + ',' + str(high) + ',' + str(low) + ',' + str(polarity) + ',' + str(subjectivity) + '\n'
            csv.write(row)


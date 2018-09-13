# from manipulation.newsAPI_manipulation import anArticle
import argparse
import datetime
from newsapi import NewsApiClient
from manipulation.newsAPI_manipulation import get_updated_articles, create_articleList
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

    from_date = dates_range['start']
    to_date = dates_range['end']

    #TODO: transfer the returned data (useful_data) to a csv file and continue from the last registered date
    article_list = create_articleList(from_date, to_date)

    #all useful dates (TODO: add sentiment analysis to the returned result)
    useful_data = link_stock_value_to_article_date(article_list)

    # print(useful_data)


# from manipulation.newsAPI_manipulation import anArticle
import argparse
from newsapi import NewsApiClient
from manipulation.newsAPI_manipulation import get_updated_articles, create_articleList
from manipulation.Stock_value_on_date import link_stock_value_to_article_date
from runner.console_monochrome import Console

parser = argparse.ArgumentParser(description='So far, collecting data for stock market prediction')
parser.add_argument('--create-csv', dest='createCSV', help='scraping articles from most recent date and applying stock market values on that day', action='store_true')
args = parser.parse_args()

CREATECSV = args.createCSV

logger = Console()

from_date = '2017-03-09'
to_date = '2018-03-09'


if CREATECSV:
    #TODO: transfer the returned data (useful_data) to a csv file and continue from the last registered date
    article_list = create_articleList(from_date, to_date)

    #all useful dates (TODO: add sentiment analysis to the returned result)
    useful_data = link_stock_value_to_article_date(article_list)

    print(useful_data)


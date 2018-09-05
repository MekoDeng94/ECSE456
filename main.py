# from manipulation.newsAPI_manipulation import anArticle
import argparse
from newsapi import NewsApiClient
from manipulation.newsAPI_manipulation import get_updated_articles, create_articleList
from runner.console_monochrome import Console

parser = argparse.ArgumentParser(description='So far, collecting data for stock market prediction')
parser.add_argument('--create-csv', dest='createCSV', help='scraping articles from most recent date and applying stock market values on that day', action='store_true')
args = parser.parse_args()

CREATECSV = args.createCSV

logger = Console()

from_date = '2018-02-14'
to_date = '2018-06-14'

# if __name__ == "__main__":
    #Get most recent articles from newsAPI (start off from most recent date)
    # print(create_articleList(from_date, to_date))
    

    #Pass it into stock_value_on_date to get the stock values on the day (returns AMD_data)

    #Pass it by sentiment analysis.

if CREATECSV:
    print(create_articleList(from_date, to_date))
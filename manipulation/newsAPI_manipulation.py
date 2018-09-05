from newsapi import NewsApiClient
from newspaper import Article
from runner.console_monochrome import Console
import json

logger = Console()

#using newsAPI to fetch relevant articles
newsapi = NewsApiClient(api_key='044f2ebd104142f4a48c5414e6f86b27')

#creating a list of articles to be passed as an object to Stock_value_on_date.py
articleList = []

class anArticle:
    articleCount = 0

    def __init__(self,url,author,date):
        self.url = url
        self.author = author
        self.date = date

    def __repr__(self):
        return "<__main__.anArticle: url = " + str(self.url) + "; author = " + str(self.author) + "; date = " + str(self.date) + ">"           

def get_updated_articles(from_date, to_date):
    #newsapi doesn't seem to be capable of handling large amounts of data.. the furthest data I could get was back to 2017..
    logger.info('Getting articles from ' + from_date + ' to ' + to_date)
    all_articles = newsapi.get_everything(q = 'AMD stock',
                                        from_param = from_date,
                                        to = to_date,
                                        language = 'en',
                                        sort_by = 'relevancy',
                                        )
    returned_articles = all_articles.get('articles',None)
    num_articles = len(returned_articles)
    logger.info('Total number of articles fetched: ' + str(num_articles))
    return returned_articles

def create_articleList(from_date, to_date):
    articles = get_updated_articles(from_date, to_date)
    articleList = []

    for article in articles:
        logger.info('Extracting article information')
        link = article.get("url")
        auth = article.get("author")
        time = article.get("publishedAt")
        sources = article.get("source")
        domain_name = sources.get("name")
        article = Article(link)
        try:
            article.download()
            article.parse()
            text = article.text
            domain_name = anArticle(link, auth, time)
            articleList.append(domain_name)
        except Exception as e:
            pass

    logger.info('Information extracted')

    return articleList

    

import json
from newsapi import NewsApiClient
from newspaper import Article
from runner.console_monochrome import Console
from textblob import TextBlob
from manipulation.text_blob import get_sentiment_polarity, get_sentiment_subjectivity

logger = Console()

#using newsAPI to fetch relevant articles
newsapi = NewsApiClient(api_key='044f2ebd104142f4a48c5414e6f86b27')

#creating a list of articles to be passed as an object to Stock_value_on_date.py
articleList = []

class anArticle:
    articleCount = 0

    def __init__(self,url,author,date, polarity, subjectivity):
        self.url = url
        self.author = author
        self.date = date
        self.polarity = polarity
        self.subjectivity = subjectivity

    def __repr__(self):
        return "<__main__.anArticle: url = " + str(self.url) + "; author = " + str(self.author) + "; date = " + str(self.date) + "; polarity = " + str(self.polarity) + "; subjectivity = " + str(self.subjectivity) + ">"           

def get_updated_articles(from_date, to_date):
    #IMPORTANT: Limit to NewsAPI is fetching 20 articles @ a time..
    logger.info('Getting articles from ' + from_date + ' to ' + to_date)
    all_articles_returned = []
    all_articles_num = 0
    page_empty = False
    num = 1
    while not page_empty:
        logger.info('Going through page' + str(num))
        all_articles = newsapi.get_everything(q = 'AMD stock',
                                            from_param = from_date,
                                            to = to_date,
                                            language = 'en',
                                            sort_by = 'relevancy',
                                            page=num
                                            )
        returned_articles = all_articles.get('articles',None)
        num_articles = len(returned_articles)

        all_articles_returned = all_articles_returned + returned_articles
        all_articles_num = all_articles_num + num_articles        

        logger.info('Number of articles fetched this batch: ' + str(num_articles))
        if num_articles == 0:
            page_empty = True
            logger.info('No more pages to go through!')
        else:
            num += 1

    logger.info ('Total number of articles fetched: ' + str(all_articles_num))
    return all_articles_returned
        
def create_articleList(from_date, to_date):
    articles = get_updated_articles(from_date, to_date)
    articleList = []

    count = 0
    for article in articles:
        count += 1
        link = article.get("url")
        auth = article.get("author")
        time = article.get("publishedAt")
        sources = article.get("source")
        domain_name = sources.get("name")
        logger.info('Extracting article information... ' + str(count))
        article = Article(link)
        try:
            article.download()
            article.parse()
            text = article.text
            sentiment_polarity = get_sentiment_polarity(text)
            sentiment_subjectivity = get_sentiment_subjectivity(text)
            domain_name = anArticle(link, auth, time, sentiment_polarity, sentiment_subjectivity)
            articleList.append(domain_name)
        except Exception as e:
            pass

    logger.info('Information extracted')

    return articleList

    

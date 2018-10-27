import json
from newsapi import NewsApiClient
from newspaper import Article
from runner.console_monochrome import Console
from textblob import TextBlob
from manipulation.vader_sentiment import get_vader_sentiment
from manipulation.text_blob import get_sentiment_polarity, get_sentiment_subjectivity
import manipulation.googleScapper as googleScapper

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

class anArticle_vader:
    articleCount = 0

    def __init__(self,url,author,date, pos, neg, neu, compound):
        self.url = url
        self.author = author
        self.date = date
        self.pos = pos
        self.neg = neg
        self.neu = neu
        self.compound = compound

    def __repr__(self):
        return "<__main__.anArticle: url = " + str(self.url) + "; author = " + str(self.author) + "; date = " + str(self.date) + "; pos = " + str(self.pos) + "; neg = " + str(self.neg) + "; neu = " + str(self.neu) + "; compound = " + str(self.compound) + ">"

def get_updated_articles(from_date, to_date):
    #IMPORTANT: Limit to NewsAPI is fetching 20 articles @ a time..
    logger.info('Getting articles from ' + from_date + ' to ' + to_date)
    all_articles_returned = []
    all_articles_num = 0
    page_empty = False
    num = 1
    while (not page_empty) and num <= 1:
        all_articles = googleScapper.get_everything(q ='AMD|Advanced Micro Devices',
                                            from_param =from_date,
                                            to = to_date,
                                            language = 'en',
                                            sort_by = 'relevancy',
                                            page=num,
                                            page_size=2
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

def create_articleList(from_date, to_date, sentiment_tool):
    articles = get_updated_articles(from_date, to_date)
    articleList = []

    count = 0
    for article in articles:
        count += 1
        link = article.get("url")
        auth = article.get("author")
        time = article.get("publishedAt")
        logger.info('Extracting article information... ' + str(count))
        article = Article(link)
        try:
            article.download()
            article.parse()
            text = article.text

            if (sentiment_tool == 'textblob'):
                sentiment_polarity = get_sentiment_polarity(text)
                sentiment_subjectivity = get_sentiment_subjectivity(text)
                domain_name = anArticle(link, auth, time, sentiment_polarity, sentiment_subjectivity)

            if (sentiment_tool == 'vader'):
                sentiment = get_vader_sentiment(text)
                domain_name = anArticle_vader(link, auth, time, 0, 0, 0, sentiment)
            articleList.append(domain_name)
        except Exception as e:
            pass

    logger.info('Information extracted')

    return articleList

def clean_articleList(articleList):
    clean_articleList = []
    currentDate = ""

    article_count_in_day = 0
    added_compound_value = 0

    for article in articleList:
        # first time
        if (currentDate == ""):
            currentDate = article.date
            article_count_in_day += 1
            added_compound_value = article.compound
        else:
            if (article.date == currentDate):
                article_count_in_day += 1
                added_compound_value += article.compound
            else:
                #compute the average
                average_compound = added_compound_value/article_count_in_day
                domain_name = anArticle_vader("NONE", "NONE", currentDate, 0,0,0, average_compound)
                clean_articleList.append(domain_name)
                article_count_in_day = 1
                added_compound_value = article.compound
                currentDate = article.date

    if (currentDate != ""):
        average_compound = added_compound_value/article_count_in_day
        domain_name = anArticle_vader("NONE", "NONE", currentDate, 0,0,0, average_compound)
        clean_articleList.append(domain_name)            
                
    return clean_articleList
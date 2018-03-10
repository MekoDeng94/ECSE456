from newsapi import NewsApiClient
from newspaper import Article
from textblob import TextBlob
import json

newsapi = NewsApiClient(api_key='044f2ebd104142f4a48c5414e6f86b27')

all_articles = newsapi.get_everything(q='AMD stock',
                                      from_parameter='2018-02-01',
                                      to='2018-02-18',
                                      language='en',
                                      sort_by='relevancy')

articles = all_articles.get('articles',None)

for article in articles:
    link = article.get("url")
    article = Article(link)
    try:
        article.download()
        article.parse()
        text = article.text
        blob = TextBlob(text)
        print(blob.sentiment)
    except Exception as e:
        pass

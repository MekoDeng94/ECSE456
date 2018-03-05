from newsapi import NewsApiClient
from newspaper import Article
import json

data = {}
data['articles'] = []

newsapi = NewsApiClient(api_key='044f2ebd104142f4a48c5414e6f86b27')

all_articles = newsapi.get_everything(q='AMD stock',
                                      from_parameter='2018-02-01',
                                      to='2018-02-18',
                                      language='en',
                                      sort_by='relevancy')

articles = all_articles.get('articles',None)

for article in articles:
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
        data['articles'].append({
        'domain name': domain_name,
        'author': auth,
        'publishedAt': time,
        'text': text
        })
    except Exception as e:
        pass

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

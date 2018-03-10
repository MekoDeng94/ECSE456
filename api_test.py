from newsapi import NewsApiClient
import json

# Init
newsapi = NewsApiClient(api_key='044f2ebd104142f4a48c5414e6f86b27')

# /v2/everything
all_articles = newsapi.get_everything(q='AMD stock',
                                      from_parameter='2018-02-01',
                                      to='2018-02-18',
                                      language='en',
                                      sort_by='relevancy')

articles = all_articles.get('articles',None)



# printing urls
for article in articles:
    sources = article.get("source")
    print(sources.get("name"))

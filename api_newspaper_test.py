from newsapi import NewsApiClient
from newspaper import Article
import json

data = {}
data['articles'] = []

#using newsAPI to fetch relevant articles
newsapi = NewsApiClient(api_key='044f2ebd104142f4a48c5414e6f86b27')

#newsapi doesn't seem to be capable of handling large amounts of data.. the furthest data I could get was back to 2017..
all_articles = newsapi.get_everything(q='AMD stock',
                                      from_parameter='2018-02-14',
                                      to='2018-02-15',
                                      language='en',
                                      sort_by='relevancy',
                                      )

articles = all_articles.get('articles',None)

#creating a list of articles to be passed as an object to Stock_value_on_date.py
articleList = []

class anArticle:
    articleCount = 0

    def __init__(self,url,author,date):
        self.url = url
        self.author = author
        self.date = date

    def addInformations(self,i):
        self.append(i) 

    def __repr__(self):
        return "<__main__.anArticle: url = " + str(self.url) + "; author = " + str(self.author) + "; date = " + str(self.date) + ">"           

def printing(self):
    return articleList
#
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
        domain_name = anArticle(link, auth, time)
        articleList.append(domain_name)
        # data['articles'].append({
        # 'domain name': domain_name,
        # 'author': auth,
        # 'publishedAt': time,
        # 'text': text
        # })
    except Exception as e:
        pass

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)

    

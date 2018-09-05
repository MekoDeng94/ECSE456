from newspaper import Article
from textblob import TextBlob
import json

url = 'http://www.valuewalk.com/2018/02/advanced-micro-devices-inc-stock-still-sliding-earnings-beat/'

article = Article(url)

article.download()

article.parse()

text = article.text

blob = TextBlob(text)

print(text)

print (blob.sentiment)


'''
https://docs.google.com/document/d/1fH8CDJoRfcPg1u39KMwq1bN02ZPKKVLMnww2SDz-TeI/edit
'''

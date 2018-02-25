from newspaper import Article
from textblob import TextBlob

url = 'http://www.valuewalk.com/2018/02/advanced-micro-devices-inc-stock-still-sliding-earnings-beat/'

article = Article(url)

article.download()

article.parse()

text = article.text

blob = TextBlob(text)

print(text)

print (blob.sentiment)

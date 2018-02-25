from newspaper import Article

link = 'www.valuewalk.com/2018/02/advanced-micro-devices-inc-stock-still-sliding-earnings-beat/'
article = Article(link)
article.download()
article.parse()
print(article.text)

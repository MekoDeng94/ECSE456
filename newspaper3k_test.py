from newspaper import Article

link = 'https://finance.yahoo.com/news/advanced-micro-devices-inc-stock-114054827.html'
article = Article(link)
article.download()
article.parse()
print(article.text)

import requests

link = "https://finance.yahoo.com/news/amd-turns-first-profit-since-020500115.html"
f = requests.get(link)

print(f.text)

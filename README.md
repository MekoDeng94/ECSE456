# The following describe the process of data collection/data manipulation
 ```
 #main.py should be used to run the scripts (maybe follow by a couple of commands)

 py main.py --create-csv
 ```
## Use News API and EventRegistry to fetchData
* NewsAPI: MAX FETCH CAPABILITY: 20 Articles
* Upon collecting data, associate stock value and price to the date of each articles

## Parsing sentiment in article
* Using VADER.sentiment and manually writing out positive.txt and negative.txt to "train" model (quite a bit of 
    work, but needs to be done)
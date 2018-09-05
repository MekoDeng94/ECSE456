# The following describe the process of data collection/data manipulation
 ```
 #main.py should be used to run the scripts (maybe follow by a couple of commands)

 py main.py
 ```
## Use News API and EventRegistry to fetchData
* Currently, NewAPI doesn't seem to be working.. (changes in the API call (unmaintained?))
* Point above: NewsAPI works, uninstall and install
* Upon collecting data, associate stock value and price to the date of each articles (done in stock_value_on_date.py)

## Parsing sentiment in article
* Using VADER.sentiment and manually writing out positive.txt and negative.txt to "train" model (quite a bit of 
    work, but needs to be done)
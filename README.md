# The following describe the process of data collection/data manipulation
 ```
 #main.py should be used to run the scripts (maybe follow by a couple of commands)

 py main.py --create-csv  - will create CSV file for articles swept in a time interval
 ```
## Update on NewsAPI
* NewsAPI only allows to go back up to <strong>a month</strong> of data!
* Alternatives include web scrapping google

## Parsing sentiment in article - vader.sentiment and Textblob
* Textblob and vader.sentiment are currently used to parse sentiment out of articles
* TODO: train these two models so that we get a more accurate sentiment.

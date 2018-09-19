from textblob import TextBlob

def get_sentiment_polarity(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def get_sentiment_subjectivity(text):
    blob = TextBlob(text)
    return blob.sentiment.subjectivity
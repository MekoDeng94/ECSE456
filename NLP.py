import os
import sys
import json

#use textblob, to download, command prompt:
#py -m pip install textblob
#py -m textblob.download_corpora

from textblob import TextBlob
from newsapi import NewsApiClient
from pprint import pprint

newsapi = NewsApiClient(api_key='12d6a0b3973b4bfd9afcb2973b1b6b22')
#first fetch file or whatever from database, then need to figure out how to parse stuff

text = '''
Advanced Micro Devices, Inc. (AMD
AMD
Advanced Micro Devices Inc
11.82
-3.04%
 
) shares entered 2017 on a high note, ascending through the final stage of a strong uptrend that posted nearly 300% gains. The stock stalled above $15.50 just two months later, spending the rest of the year disappointing shareholders who expected AMD to keep pace with much larger rival NVIDIA Corporation (NVDA
NVDA
NVIDIA Corp
243.84
-1.08%
 
). Even worse, price action has settled into an annual loss, raising the odds that end-of-year tax selling pressure will take control in the coming weeks.

Read more: AMD Stock May Be Headed for Single Digits | Investopedia https://www.investopedia.com/news/amd-stock-may-be-headed-single-digits/#ixzz57TdAdxEt 
Follow us: Investopedia on Facebook
'''

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

#The polarity score is a float within the range [-1.0, 1.0]. 
#The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
#not sure if this is the best way, but should test it out
print (blob.sentiment)
# for sentence in blob.sentences:
#     print(sentence.sentiment)

# 0.060
# -0.341


blob.translate(to="es")  # 'La amenaza titular de The Blob...'

all_articles = newsapi.get_everything(q='amd',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_parameter='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy')


data = all_articles

with open ("data.json","w") as outfile:
	json.dump(data,outfile)

with open ('data.json') as data_file:
	retrieved = json.load(data_file)
pprint(retrieved)
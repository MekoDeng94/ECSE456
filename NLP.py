import os
import sys

#use textblob, to download, command prompt:
#py -m pip install textblob
#py -m textblob.download_corpora

from textblob import TextBlob

#first fetch file or whatever from database, then need to figure out how to parse stuff

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
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

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341


blob.translate(to="es")  # 'La amenaza titular de The Blob...'


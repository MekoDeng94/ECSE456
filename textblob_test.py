import os
import sys
from textblob import TextBlob

text = '''

Jeremy is beautiful.
Jeremy is an idiot though.
Jeremy is failing all his classes.
I love Jeremy.

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


print(blob.sentiment)

# 0.060

# -0.341

blob.translate(to="es")  # 'La amenaza titular de The Blob...'

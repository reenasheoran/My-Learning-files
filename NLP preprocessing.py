# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
#nltk.download()
paragraph="""I have three visions for India. In 3000 years of our history people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture and their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others. That is why my FIRST VISION is that of FREEDOM. I believe that India got its first vision of this in 1857, when we started the war of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us.

We have 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect? MY SECOND VISION for India is DEVELOPMENT. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among top five nations in the world in terms of GDP.

I have a THIRD VISION. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand. My good fortune was to have worked with three great minds. Dr.Vikram Sarabhai, of the Dept. of Space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.

I was in Hyderabad giving this lecture, when a 14 year-old girl asked me for my autograph. I asked her what her goal in life is. She replied: I want to live in a developed India. For her, you and I will have to build this developed India. You must proclaim India is not an underdeveloped nation; it is a highly developed nation.

You say that our government is inefficient. You say that our laws are too old. You say that the municipality does not pick up the garbage. You say that the phones don’t work, the railways are a joke, the airline is the worst in the world, and mails never reach their destination. You say that our country has been fed to the dogs and is the absolute pits. You say, say and say. What do you do about it?

Dear Indians, I am echoing J.F.Kennedy’s words to his fellow Americans to relate to Indians ……. “ASK WHAT WE CAN DO FOR INDIA AND DO WHAT HAS TO BE DONE TO MAKE INDIA WHAT AMERICA AND OTHER WESTERN COUNTRIES ARE TODAY."""

 
# stemming
from nltk.stem  import PorterStemmer
from nltk.corpus import stopwords
sentences=nltk.sent_tokenize(paragraph)
#words=nltk.word_tokenize(paragraph)
stemmer=PorterStemmer()

# Stemming with list comprehension
for i in range(len(sentences)):
    words= nltk.word_tokenize(sentences[i])
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i]=" ".join(words)
    
# Lemmatization
# import nltk
from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords

Lsentences=nltk.sent_tokenize(paragraph)
lemmatizer=WordNetLemmatizer()

for i in range(len(sentences)):
    Lwords= nltk.word_tokenize(Lsentences[i])
    Lwords=[lemmatizer.lemmatize(word) for word in Lwords if word not in set(stopwords.words("english"))]
    Lsentences[i]=" ".join(Lwords)
    
    
# Bag of words with stemming
# import nltk
    
# text cleaning
import re
# =============================================================================
# from nltk.stem.porter import PorterStemmer
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords

# =============================================================================
ps=PorterStemmer()
corpus=[]
for i in range(len(sentences)):
    review=re.sub("[^a-zA-Z]",' ',sentences[i])
    review=review.lower()
    review= review.split()
    review=[ps.stem(word) for word in review if word not in set(stopwords.words("english"))]
    review=" ".join(review)
    corpus.append(review)

# create bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
x=cv.fit_transform(corpus).toarray()

# Bag of words with lemmatizing
# import nltk
    
# text cleaning
#import re
# =============================================================================
# from nltk.stem.porter import PorterStemmer
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
#sentences=nltk.sent_tokenize(paragraph)
# =============================================================================
NLsentences=nltk.sent_tokenize(paragraph)

lm=WordNetLemmatizer()
Lcorpus=[]
for i in range(len(NLsentences)):
    Lreview=re.sub("[^a-zA-Z]",' ',NLsentences[i])
    Lreview=Lreview.lower()
    Lreview= Lreview.split()
    Lreview=[lm.lemmatize(word) for word in Lreview if word not in set(stopwords.words("english"))]
    Lreview=" ".join(Lreview)
    Lcorpus.append(Lreview)

# create bag of words
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
x1=cv.fit_transform(Lcorpus).toarray()

# TFIDF vectorization with lemmatization
# it can be done with stemming also

# import nltk
    
# text cleaning
#import re
# =============================================================================
# from nltk.stem.porter import PorterStemmer
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
#sentences=nltk.sent_tokenize(paragraph)
# =============================================================================
TLsentences=nltk.sent_tokenize(paragraph)

lm=WordNetLemmatizer()
TLcorpus=[]
for i in range(len(TLsentences)):
    TLreview=re.sub("[^a-zA-Z]",' ',TLsentences[i])
    TLreview=TLreview.lower()
    TLreview= TLreview.split()
    TLreview=[lm.lemmatize(word) for word in TLreview if word not in set(stopwords.words("english"))]
    TLreview=" ".join(TLreview)
    TLcorpus.append(TLreview)

# create bag of words
from sklearn.feature_extraction.text import TfidfVectorizer
Tfv=TfidfVectorizer()
x2=Tfv.fit_transform(TLcorpus).toarray()

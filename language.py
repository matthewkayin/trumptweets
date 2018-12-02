import os
import nltk
import data_collection as dc
from nltk.grammar import CFG
from nltk.parse import CoreNLPParser
from nltk.parse.generate import generate
from random import randint

tweet_text_data = dc.get_cleaned_up_tweet_text_data()
max_tweets = 2934
tweets = tweet_text_data.split("\n")
corpus = dc.create_corpus_from_text_data(text_data=tweet_text_data,
                                         max_lines=max_tweets)

quote = "Incredible to be with our GREAT HEROES today in California."
parser = CoreNLPParser(url='http://localhost:9000')
#sentences = parser.raw_parse('Incredible to be with our GREAT HEROES today in California.')

sentences = []
range = 20
upper = randint(range, len(tweets))
lower = upper - range
for i in range(lower, upper):
    print(i)
    sentences += parser.raw_parse(tweets[i])
#sentences += parser.raw_parse(tweets[0])

productions = []
for s in sentences:
    productions += s.productions()

grammar = CFG(nltk.Nonterminal('ROOT'), productions)
print(grammar)

new_tweets = []
for sentence in generate(grammar, depth=8, n=100):
    string = ' '.join(sentence)
    if not string in new_tweets:
        new_tweets.append(string)
        print(string)

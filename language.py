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

sentences = []
productions = []
min_num_tweets = 30
end_index = randint(min_num_tweets, len(tweets))
start_index = end_index - min_num_tweets
for i in range(start_index, end_index):
    print(f"Parsing tweet number {i}")
    sentence = parser.raw_parse(tweets[i])
    sentences += sentence
for sentence in sentences:
    productions += sentence.productions()

grammar = CFG(nltk.Nonterminal('ROOT'), productions)
print(grammar)

new_tweets = []
depth = 8
number_of_productions = 20

for sentence in generate(grammar, depth=depth, n=number_of_productions):
    string = ' '.join(sentence)
    if not string in new_tweets:
        new_tweets.append(string)
        print("Generated unique tweet:")
        print(string)

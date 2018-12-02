import os
import nltk
import data_collection as dc
from nltk.grammar import CFG
from nltk.parse import CoreNLPParser
from nltk.parse.generate import generate
from random import randint
import os

if os.name == "nt":
    tweets = dc.get_cleaned_up_tweet_text_data(filename="trump_tweets_ansi.txt",
                                               get_text=dc.get_tweet_text_data_ansi)
else:
    tweets = dc.get_cleaned_up_tweet_text_data()

max_tweets = 2934
# tweets = tweet_text_data.split(".")
total_num_tweets = len(tweets)

quote = "Incredible to be with our GREAT HEROES today in California."
parser = CoreNLPParser(url='http://localhost:9000')

sentences = []
all_productions = []
used_tweet_nums = []
sample_num_tweets = 25
for count in range(sample_num_tweets):
    random_index = randint(0, total_num_tweets)
    while random_index in used_tweet_nums:
        random_index = randint(0, total_num_tweets)
    used_tweet_nums.append(random_index)
    print(f"Parsing tweet number {random_index}:")
    print(tweets[random_index])
    sentence = parser.raw_parse(tweets[random_index])
    sentences += sentence
for sentence in sentences:
    productions = sentence.productions()
    if productions not in all_productions:
        all_productions += productions

grammar = nltk.grammar.CFG(nltk.Nonterminal('ROOT'), all_productions)
print(grammar)

new_tweets = []
for sentence in generate(grammar, depth=10, n=25):
    string = ' '.join(sentence)
    if not string in new_tweets:
        new_tweets.append(string)
        print("Generated unique tweet:")
        print(string)

import os
import nltk
import data_collection as dc
from nltk.grammar import CFG
from nltk.parse import CoreNLPParser
from nltk.parse.generate import generate
from random import randint, choice
import os

def is_repeating(string):
    words = string.split(" ")
    for word in words:
        if string.count(word) > 2:
            return True
    return False

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
productions = []
min_num_tweets = 10
end_index = randint(min_num_tweets, len(tweets))
start_index = end_index - min_num_tweets
for i in range(start_index, end_index):
    print(f"Parsing tweet number {i}")
    sentence = parser.raw_parse(tweets[i])
    sentences += sentence
productions = []
for sentence in sentences:
    productions = sentence.productions()
    if productions not in all_productions:
        all_productions += productions

# nltk.grammar.CFG
grammar = nltk.grammar.induce_pcfg(nltk.Nonterminal('ROOT'), all_productions)
print(grammar)
print(all_productions)

for p in productions:
    print(p)
new_tweets = []

for sentence in generate(grammar, depth=10, n=100):
    string = ' '.join(sentence)
    if not string in new_tweets:
        if not is_repeating(string):
            new_tweets.append(string)
            print("Generated unique tweet:")
            print(string)


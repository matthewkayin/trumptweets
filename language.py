import os
import nltk
import data_collection as dc
from nltk.grammar import CFG
from nltk.parse import CoreNLPParser
from nltk.parse.generate import generate
from random import randint, choice
import os

def isRepetitive(sentence):
    words = sentence.split(' ')
    numberOfRepeats = 0
    for i in range(0, len(words)):
        count = words.count(words[i])
        if count > 2:
            numberOfRepeats += 1
    if numberOfRepeats > 3:
        return True
    else:
        return False

def createSentence(productions, start):
    newString = []
    #print("start = " + str(start))
    for token in start:
        #print("for token " + str(token))
        validProductions = []
        for production in productions:
            if str(production.lhs()) == str(token):
    #            print("valid production found! = " + str(production))
                validProductions.append(production)
        if not len(validProductions) == 0:
            toUse = choice(validProductions)
    #        print("chosen to use production " + str(toUse))
            rhs = toUse.rhs()
            for t in rhs:
    #            print("adding to string token " + str(t))
                newString.append(t)
        else:
            newString.append(token)
    #print("newString = " + str(newString))
    finished = True
    for token in newString:
        if str(token).isalpha():
            if str(token).upper() == str(token):
                finished = False
                break
    if finished:
        rVal = ""
        for token in newString:
            if str(token) == ".":
                rVal += str(token)
            else:
                rVal += str(token)
                rVal += " "
        return rVal
    else:
        return createSentence(productions, newString)

if os.name == "nt":
    tweet_text_data = dc.get_cleaned_up_tweet_text_data(filename="trump_tweets_ansi.txt",
                                                        get_text=dc.get_tweet_text_data_ansi)
else:
    tweet_text_data = dc.get_cleaned_up_tweet_text_data()

max_tweets = 2934
tweets = tweet_text_data.split("\n")

corpus = dc.create_corpus_from_text_data(text_data=tweet_text_data,
                                         max_lines=max_tweets)
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
    if not sentence.productions() in productions:
        productions += sentence.productions()

for p in productions:
    print(p)
new_tweets = []
for i in range(0, 10):
    nt = createSentence(productions, ['ROOT'])
    new_tweets.append(nt)
for nt in new_tweets:
    print(nt)

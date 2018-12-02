import data_collection as dc
from gensim.models.phrases import Phrases
import random

tweet_text_data = dc.get_cleaned_up_tweet_text_data()
max_tweets = 2934

tweets = tweet_text_data.split("\n")
print(len(tweets))
corpus = dc.create_corpus_from_text_data(text_data=tweet_text_data,
                                         max_lines=max_tweets)
print(len(corpus))

model = dc.create_word2vec_model(corpus=corpus, frequency=10, freedom=25, iterations=10)

print(model)

new_tweet = []
seed_word = "democrats"
num_choices = 5
max_words = 10
current_num_words = 0
current_word = seed_word
while (True):
    similar_words = model.most_similar(positive=[current_word], topn=num_choices)
    random_selection_index = random.randint(0, num_choices - 1)
    next_word, similarity = similar_words[random_selection_index]
    if next_word in new_tweet:
        continue
    new_tweet.append(current_word)
    print(f"Chose word with similarity of {similarity}")
    current_word = next_word
    current_num_words += 1
    if current_num_words >= max_words:
        break

print("Constructed tweet:")
print(" ".join(new_tweet))

from textgenrnn import textgenrnn
import data_collection as dc
import os
# import language_check
from random import randint

def pick_random_sample(tweets: list, number_to_pick: int):
    total_num_tweets = len(tweets)
    used_tweets = []
    picked_tweets = []
    for count in range(0, number_to_pick):
        random_index = randint(0, total_num_tweets - 1)
        while(random_index in used_tweets):
            random_index = randint(0, total_num_tweets)
        print(f"Using tweet number {random_index}")
        # print(tweets[random_index])
        used_tweets.append(random_index)
        picked_tweets.append(tweets[random_index])
    return picked_tweets


# get_text_data_no_sentence_split
# get_text_data_less_clean
if os.name == "nt":
    tweets = dc.get_text_data_no_sentence_split(filename="trump_tweets_ansi.txt",
                                         get_text=dc.get_tweet_text_data_ansi)
else:
    tweets = dc.get_text_data_no_sentence_split()

# tool = language_check.LanguageTool('en-US')
seed_word = None
degree_freedom = 0.2
dropout = 0
num_epochs = 25
num_gen_epochs = 5
tweet_length = 140
# tweets_to_use = pick_random_sample(tweets=tweets, number_to_pick=100)
tweets_to_use = tweets
textgen = textgenrnn()
textgen.reset()

# textgen.train_from_file("trump_tweets.txt", num_epochs=1)
textgen.train_on_texts(tweets_to_use,
                       num_epochs=num_epochs,
                       gen_epochs=num_gen_epochs,
                       dropout=dropout,
                       max_gen_length=tweet_length)

output = textgen.generate(3,
                          prefix=seed_word,
                          temperature=degree_freedom,
                          return_as_list=True,
                          max_gen_length=tweet_length)

print("========Training Complete========")
textgen.generate_samples()
for tweet in output:
    print(f"Tweet before grammar check:\n {tweet}\n")
    # matches = tool.check(tweet)
    # corrected_tweet = language_check.correct(tweet, matches)
    # print(f"Tweet after grammar check:\n {corrected_tweet}\n")

textgen.save("25_epochs_all_tweet_weights.hdf5")

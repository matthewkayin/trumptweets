from textgenrnn import textgenrnn
import data_collection as dc
import os

if os.name == "nt":
    tweets = dc.get_cleaned_up_tweet_text_data(filename="trump_tweets_ansi.txt",
                                               get_text=dc.get_tweet_text_data_ansi)
else:
    tweets = dc.get_cleaned_up_tweet_text_data()

textgen = textgenrnn()
textgen.generate()

# textgen.train_from_file("trump_tweets.txt", num_epochs=1)
textgen.train_on_texts(tweets[0:50], num_epochs=2,  gen_epochs=2)
output = textgen.generate(1, prefix="I", temperature=0.7, return_as_list=True)
print(output)

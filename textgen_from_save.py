from textgenrnn import textgenrnn
import sys

# python textgen_from_save.py number_of_tweets seed_string degree_freedom
#                               int             string      float
print(sys.argv)
filename, num_tweets, seed, degree_freedom = sys.argv

if seed == "None":
    seed = None

tweet_length = 140
textgen = textgenrnn()
textgen.reset()

# textgen.train_from_file("trump_tweets.txt", num_epochs=1)
textgen.load("25_epochs_all_tweet_weights.hdf5")

output = textgen.generate(int(num_tweets),
                          prefix=seed,
                          temperature=float(degree_freedom),
                          return_as_list=True,
                          max_gen_length=tweet_length)

print("========Training Complete========")
for tweet in output:
    print(tweet)


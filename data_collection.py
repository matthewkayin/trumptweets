import gensim

def get_tweet_text_data(filename = "trump_tweets.txt"):
    with open("trump_tweets.txt") as file:
        tweet_text = file.read()
    return tweet_text


def get_cleaned_up_tweet_text_data(filename = "trump_tweets.txt"):
    tweet_text = get_tweet_text_data(filename=filename)
    tweet_text = tweet_text.replace("...", ".")
    tweet_text = tweet_text.replace(". . .", ".")
    tweet_text = tweet_text.replace(",", "")
    tweet_text = tweet_text.replace("!", ".")
    tweet_text = tweet_text.replace("?", ".")
    tweet_text = tweet_text.replace("\"", "")
    tweet_text = tweet_text.replace("“", "")
    tweet_text = tweet_text.replace("”", "")
    tweet_text = tweet_text.replace("–", "")
    tweet_text = tweet_text.replace("-", "")
    tweet_text = tweet_text.replace("—", "")
    tweet_text = tweet_text.replace(")", "")
    tweet_text = tweet_text.replace("(", "")
    
    tweet_text = tweet_text.lower()
    return tweet_text


"""
def create_vocabulary_from_text_data(text_data, max_lines = None):
    vocabulary = []
    lines_read = 0
    lines = text_data.split("\n")
    if max_lines is None:
        max_lines = len(lines)

    for line in lines:
        words = line.split(" ")
        for word in words:
            if word.startswith("http") or word.startswith("@"):
                continue
            if "http" in word:
                link_start_index = word.index("http")
                word = word[:link_start_index]
            if word not in vocabulary:
                vocabulary.append(word)
        lines_read += 1
        if lines_read >= max_lines:
            break

    return vocabulary


def create_bag_of_words_from_lines(lines_of_text, vocab):
    bag_of_words = []

    for line in lines_of_text:
        bag = [0 for i in range(len(vocab))]
        words = line.split(" ")
        for word in words:
            try:
                index = vocab.index(word)
            except ValueError:
                continue
            bag[index] += 1
        bag_of_words.append(bag)

    return bag_of_words


def create_bag_of_words_from_text_data(text_data, vocab):
    lines_of_text = text_data.split("\n")
    return create_bag_of_words_from_lines(lines_of_text, vocab)


def create_follows_count_vector(lines_of_text, vocab):
    follows_count_vector = [[0 for i in range(len(vocab))] for j in range(len(vocab))]

    for index_in_count_vector in range(len(vocab)):
        current_word = vocab[index_in_count_vector]
        for line in lines_of_text:
            words = line.split(" ")
            index_in_current_line = words.index(current_word)



            # find all instances in line
            # find words that follow that word in that line
            # add 1 to count in follows_count_vector for words that follow current_word
            # do ^ for all instance in the line
            # go to next line
            # after doing all lines, go to next word in vocab
"""


def split_line_into_sentences(line: str):
    if "." in line:
        sentences = line.split(".")
    else:
        sentences = [line]
    return sentences

     
def create_corpus_from_text_data(text_data, max_lines = None):
    corpus = []
    lines_read = 0
    lines = text_data.split("\n")
    if max_lines is None:
        max_lines = len(lines)

    for line in lines:
        for sentence in split_line_into_sentences(line):
            words = sentence.split(" ")
            word_array = []
            for word in words:
                if word.startswith("http") or word.startswith("@"):
                    continue
                if "http" in word:
                    link_start_index = word.index("http")
                    word = word[:link_start_index]
                if word not in word_array:
                    word_array.append(word)
            corpus.append(word_array)
        lines_read += 1
        if lines_read >= max_lines:
            break

    return corpus


def create_dictionary_gensim(text_data, max_lines=None):
    corpus = create_corpus_from_text_data(text_data, max_lines)
    dictionary = gensim.corpora.Dictionary(corpus)
    return dictionary


def create_word2vec_model(corpus, freedom = 100, frequency = 5, iterations = 5):
    model = gensim.models.Word2Vec(iter=iterations, min_count=frequency, size=freedom)
    model.build_vocab(corpus)
    return model


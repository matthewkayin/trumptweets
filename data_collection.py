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
                if word != "":
                    word_array.append(word)
            if word_array != [''] and word_array != []:
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


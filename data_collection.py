import gensim

def get_tweet_text_data(filename = "trump_tweets.txt"):
    with open(filename, encoding="utf8") as file:
        tweet_text = file.read()
    return tweet_text

def get_tweet_text_data_ansi(filename = "trump_tweets_ansi.txt"):
    with open(filename) as file:
        tweet_text = file.read()
    return tweet_text

def remove_hyperlink(string):
    word_list = []
    for word in string.split(" "):
        if word.startswith("http"):
            continue
        word_list.append(word)
    return " ".join(word_list)


def get_cleaned_up_tweet_text_data_less_clean(filename = "trump_tweets.txt", get_text=get_tweet_text_data):
    tweet_text = get_text(filename=filename)
    tweet_text = tweet_text.lower()
    tweet_text = tweet_text.replace("....", " ")
    tweet_text = tweet_text.replace("...", " ")
    tweet_text = tweet_text.replace(". . .", " ")
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
    tweet_text = tweet_text.replace("t.co", "")
    tweet_text = tweet_text.replace("u.s.", "us")
    tweet_text = tweet_text.replace("u.s.a.", "usa")
    tweet_text = tweet_text.replace("jr.", "jr")
    tweet_text = tweet_text.replace("&amp;", "&")
    tweet_text = tweet_text.replace("\n", " ")

    sentences = []
    for potential_sentence in tweet_text.split("."):
        potential_sentence = remove_hyperlink(potential_sentence)
        potential_sentence = potential_sentence.strip()
        if potential_sentence != "" and potential_sentence != " ":
            sentences.append(potential_sentence.replace(".", ""))
    
    return sentences


def get_cleaned_up_tweet_text_data_less_clean(filename = "trump_tweets.txt", get_text=get_tweet_text_data):
    tweet_text = get_text(filename=filename)

    tweet_text = tweet_text.replace("....", " ")
    tweet_text = tweet_text.replace("...", " ")
    tweet_text = tweet_text.replace(". . .", " ")
    tweet_text = tweet_text.replace("!", ".")
    tweet_text = tweet_text.replace("?", ".")
    tweet_text = tweet_text.replace("t.co", "")
    tweet_text = tweet_text.replace("u.s.", "us")
    tweet_text = tweet_text.replace("u.s.a.", "usa")
    tweet_text = tweet_text.replace("jr.", "jr")
    tweet_text = tweet_text.replace("&amp;", "&")
    tweet_text = tweet_text.replace("\n", " ")

    sentences = []
    for potential_sentence in tweet_text.split("."):
        potential_sentence = remove_hyperlink(potential_sentence)
        potential_sentence = potential_sentence.strip()
        if potential_sentence != "" and potential_sentence != " ":
            # .replace(".", "")
            sentences.append(potential_sentence)
    
    return sentences


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


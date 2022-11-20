from keras.preprocessing.text import Tokenizer
from operator import itemgetter

separators = ['\n', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', ',']


def count_words(file, n):  # file - filename, n - number of words to display
    with open(file, encoding="utf-8") as f:
        text = f.read()
    t = Tokenizer(filters=separators,lower=True,split=" ")
    t.fit_on_texts(text)
    word_list = sorted(t.word_counts.items(), key=itemgetter(1), reverse=True)
    while word_list[n][1] == word_list[n + 1][1]:  # działa, sprawdzone poprzez usunięcie reverse=True
        n = n + 1
    return print("Word Count:", word_list[:n])


count_words("potop.txt", 20)

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import normalize, tokenize, count_freq, top_n

def text_stata(textik, flag=False):

    norm_text = normalize(textik)
    token_text = tokenize(norm_text)
    word_freq = count_freq(token_text)

    if flag == False:

        words_num = len(token_text)
        unique_num = len(word_freq)
        top_5 = top_n(word_freq)

        return f"Всего слов: {words_num}\nУникальных слов: {unique_num}\nТоп-5: \n{"\n".join([":".join([i[0], str(i[1])]) for i in top_5])}"

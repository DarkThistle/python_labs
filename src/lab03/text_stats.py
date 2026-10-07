import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import normalize, tokenize, count_freq, top_n

def text_stats(textik, flag=False):

    norm_text = normalize(textik)
    token_text = tokenize(norm_text)
    word_freq = count_freq(token_text)

    words_num = len(token_text)
    unique_num = len(word_freq)
    top_5 = top_n(word_freq)
    
    if flag == False:
        top_pyat = "\n".join([":".join([i[0], str(i[1])]) for i in top_5])

        return f"Всего слов: {words_num}\nУникальных слов: {unique_num}\nТоп-5: \n{top_pyat}"
    
    max_len = max(max([len(i[0]) for i in top_5]), len("слово"))
    max_len_len = max(max([len(str(len(i[0]))) for i in top_5]), len('частота'))

    first_line = "слово".ljust(max_len) + " | " + "частота".ljust(max_len_len)
    second_line = "-" * max_len + "---" + "-" * max_len_len
    other_lines = "\n".join([i[0].ljust(max_len) + " | " + str(i[1]).ljust(max_len_len) for i in top_5])
    
    return f'{first_line}\n{second_line}\n{other_lines}'

print(text_stats(input("Ввод: "), flag=[True, False][input("Табличный режим: ").lower() == "false"]))
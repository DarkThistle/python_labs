import sys
import os

# Получаем абсолютный путь к папке src (на уровень выше lab03)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import normalize, tokenize, count_freq, top_n

best_input_in_our_universe = normalize(input())
table_switcher = input().strip() == "True"
words_num = len(tokenize(best_input_in_our_universe))
unique_num = len(count_freq(tokenize(best_input_in_our_universe)))
top_5 = top_n(count_freq(tokenize(best_input_in_our_universe)))
if not table_switcher:
    print(
        f"Всего слов: {words_num}",
        f"Уникальных слов: {unique_num}",
        f"Топ-5: \n{"\n".join([":".join([i[0], str(i[1])]) for i in top_5])}",
        sep="\n"
        )
    
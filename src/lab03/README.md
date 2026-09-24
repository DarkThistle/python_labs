# ЛР3 — Тексты и частоты слов (словарь/множество)

---

## Задание A — src/lib/text.py

---

### Функция **normalize**

В этой функции я проверил аргумент функции **casefold**, если он равен **True**, переводим текст в нижний регистр. Если **yo2e** равно **True**, программа заменяет все буквы ё/Ё на е/Е. Вконце я заменил все управляющие символы \t, \r, \n на пробел. В конце я преобразовал текст в список, а потом соединил все обратно в строку.

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.replace("\\t", " ").replace("\\r", " ").replace("\\n", " ").split()

    return " ".join(text)
```

![test1](/images/lab03/normalize_1.png)
![test1](/images/lab03/normalize_2.png)
![test1](/images/lab03/normalize_3.png)
![test1](/images/lab03/normalize_4.png)


---

### Функция **tokenize**

Тут я перебрал циклом поданный текст и проверил, чтобы символ тире не оказался в начале или в конце слов. Потом убрал все символы, которые не являются буквами или цифрами. В конц вывел список слов строки.

```python
def tokenize(text: str) -> list[str]:
    for i in range(len(text)):
        if text[i] == "-" and text[i-1].isalnum() and text[i+1].isalnum() and i not in [0, len(text)-1]:
            continue
        if text[i].isalnum():
            continue
        else:
            text = text.replace(text[i], " ")
    return text.split()
```

![test1](/images/lab03/tokenize_1.png)
![test1](/images/lab03/tokenize_2.png)
![test1](/images/lab03/tokenize_3.png)
![test1](/images/lab03/tokenize_4.png)
![test1](/images/lab03/tokenize_5.png)

---

### Функция **count_freq**

В этой функции я вывел словарь, ключами которого являются слова, полученные сортировкой униальных слов входного списка, а значениями - их частота появления в входном списке.

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    tokens = dict(zip(sorted(set(tokens)), [tokens.count(i) for i in sorted(set(tokens))]))
    return tokens
```

![test1](/images/lab03/count_freq_1.png)
![test1](/images/lab03/count_freq_2.png)

---

### Функция **top_n**

Здесь я создал пустой список **res** и счетчик **с**. Далее сначала прошел циклом по значениям отсортированного входного словаря и потом уже по ключам того же словаря. И если значение **i** совпадало со значением ключа **freq[j]**, в список **res** записывался кортеж, состоящий из слова и его частоты появления, и к счетчику прибавлялась единица. В конце, если счетчик совпадет с аргументом **n**, цикл прерывается.

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    res = []
    c = 0
    flag = False
    for i in sorted(set(freq.values()), reverse=True):
        for j in freq:
            if freq[j] == i:
                res.append((j,i))
                c += 1
            if c == n:
                break
    return res
```

![test1](/images/lab03/top_n_1.png)
![test1](/images/lab03/top_n_2.png)

---

## Задание B — src/text_stats.py

---

### Функция **transpose**

Тут я сначала завел 3 переменные, которым присвоил результат функций из задания **text.py**. Далее создал еще три переменные, в первой длина текста **token_text**, во второй длина **word_freq** и в третьей топ 5 самых частовтречаемых слов переменной **word_freq**. Потом следует часть кода, которая выводит сколько всего слов, сколько уникальных слов и топ 5 популярных слов.

```python
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

        return f"Всего слов: {words_num}\nУникальных слов: {unique_num}\nТоп-5: \n{"\n".join([":".join([i[0], str(i[1])]) for i in top_5])}"

    max_len = max(max([len(i[0]) for i in top_5]), len("слово"))
    max_len_len = max(max([len(str(len(i[0]))) for i in top_5]), len('частота'))

    return f'{"слово".ljust(max_len) + " | " + "частота".ljust(max_len_len)}\n{"-" * max_len + "---" + "-" * max_len_len}\n{"\n".join([i[0].ljust(max_len) + " | " + str(i[1]).ljust(max_len_len) for i in top_5])}'

print(text_stats(input("Ввод: "), flag=[True, False][input("Табличный режим: ").lower() == "false"]))
```

![test1](/images/lab03/table_text_stats_1.png)
![test1](/images/lab03/text_stats_2.png)

---

### ★ Дополнительно (со звёздочкой)

В выше описанный код я добавил способ вывода наиболее встречаемых слов в виде таблицы.

![test1](/images/lab03/text_stats_1.png)
![test1](/images/lab03/table_text_stats_2.png)

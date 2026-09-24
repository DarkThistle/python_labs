# ЛР3 — Тексты и частоты слов (словарь/множество)

---

## Задание A — src/lib/text.py

---

### Функция **normalize**

В этой функцие я проверил длину словаря на наличие элементов и написал вызов ошибки при их отстуствии. Далее я просто вернул минимальное и максимальное значение через запятую, что на выходе создает кортеж из этих элементов.

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

Тут я просто вернул отсортированное множество элементов списка **nums**.

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

Тут я прошел циклом по матрице, проверяя тип элементов. Если элемнет не являлся матрицей или кортежем, я вызывал ошибку. В ином случае расширял список **res** элементами исходного списка.

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    tokens = dict(zip(sorted(set(tokens)), [tokens.count(i) for i in sorted(set(tokens))]))
    return tokens
```

![test1](/images/lab03/count_freq_1.png)
![test1](/images/lab03/count_freq_2.png)

---

### Функция **top_n**

Тут я прошел циклом по матрице, проверяя тип элементов. Если элемнет не являлся матрицей или кортежем, я вызывал ошибку. В ином случае расширял список **res** элементами исходного списка.

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

## Задание В

---

### Функция **transpose**

В этой функции я сначала проверил длину списка, если он пустой, то функция возвращает []. Далее проверил длину каждой строки списка, закинул в кортеж и сравнил с единицей. Если строки в матрице имеют неравное количество символов, то функция вызывает ошибку. Далее я вложенными циклами создал создал такую матрицу, какая бы получилась путем транспонирования исходной.

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    trans = []
    if len(mat) == 0:
        return []
    if len(set(map(lambda x: len(x), mat))) > 1:
        raise ValueError
    return [[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]
```

![test1](/images/lab02/transpose_1.png)
![test2](/images/lab02/transpose_2.png)
![test3](/images/lab02/transpose_3.png)
![test4](/images/lab02/transpose_4.png)
![test5](/images/lab02/transpose_5.png)

---

### Функция **row_sums**

Тут я снова проверил матрицу на наличие неравных строк, если они есть, функция вызывает ошибку. Потом вернул список, содержащий функцию **map** применяющюю сумирование элементов к каждой строке исходной матрицы.

```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(set(map(lambda x: len(x), mat))) > 1:
            raise ValueError
    return list(map(lambda x: sum(x), mat))
```
![test1](/images/lab02/row_sums_1.png)
![test2](/images/lab02/row_sums_2.png)
![test3](/images/lab02/row_sums_3.png)
![test4](/images/lab02/row_sums_4.png)

---

### Функция **col_sums**

Здесь с помощью условия определил "рваная" матрица или нет. И потом ко всем строкам транспонированной исходной матрицы применил функцию **sum**.

```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(set(map(lambda x: len(x), mat))) > 1:
                raise ValueError
    return [sum([mat[j][i] for j in range(len(mat))]) for i in range(len(mat[0]))]
```
![test1](/images/lab02/col_sums_1.png)
![test2](/images/lab02/col_sums_2.png)
![test3](/images/lab02/col_sums_3.png)
![test4](/images/lab02/col_sums_4.png)

---

## Задание С

---

### Функция **format_record**

В этой функции я сначала проверил данные на корректность. Первые два элемента я сравнил с пустой строкой, и если они совпадают, функция вызывает ошибку **ValueError**. Если тип третьего элемента не вещественный, то происходит вызов ошибки **TypeError**. Далее я озаглавил первую букву в каждом слове превого элемента, превратив его в список и применив функцию **capitalize** к ФИО. В конце собрал все элементы в **f-строку** и вывел на экран.

```python
def format_record(rec: tuple[str, str, float]) -> str:
    if rec[0] == "" or rec[1] == "":
        raise ValueError
    if type(rec[2]) != float:
        raise TypeError
    name = [i.capitalize() for i in rec[0].split()]
    return f"{name[0]} {" ".join([i[0]+"." for i in name[1:]])}, гр. {rec[1]}, GPA {rec[2]:.02f}"
```

![test1](/images/lab02/format_record_1.png)
![test2](/images/lab02/format_record_2.png)
![test3](/images/lab02/format_record_3.png)
![test4](/images/lab02/format_record_4.png)
![test5](/images/lab02/format_record_5.png)
![test6](/images/lab02/format_record_6.png)
![test7](/images/lab02/format_record_7.png)
![test8](/images/lab02/format_record_8.png)
![test9](/images/lab02/format_record_9.png)
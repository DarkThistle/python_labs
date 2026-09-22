# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

---

## Задание 1

При счете данных я использовал функцию **eval**, которая преобразовывает строку в определенные типы данных.

---

### Функция **min_max**

В этой функцие я проверил длину словаря на наличие элементов и написал вызов ошибки при их отстуствии. Далее я просто вернул минимальное и максимальное значение через запятую, что на выходе создает кортеж из этих элементов.

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    return max(nums), min(nums)
```

![](/images/lab02/min_max_1.png)
![](/images/lab02/min_max_2.png)
![](/images/lab02/min_max_3.png)
![](/images/lab02/min_max_4.png)
![](/images/lab02/min_max_5.png)

---

### Функция **unique_sorted**

Тут я просто вернул отсортированное множество элементов списка **nums**.

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))
```

![](/images/lab02/unique_sorted_1.png)
![](/images/lab02/unique_sorted_2.png)
![](/images/lab02/unique_sorted_3.png)
![](/images/lab02/unique_sorted_4.png)

---

### Функция **flatten**

Тут я прошел циклом по матрице, проверяя тип элементов. Если элемнет не являлся матрицей или кортежем, я вызывал ошибку. В ином случае расширял список **res** элементами исходного списка.

```python
def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if type(i) is not list and type(i) is not tuple:
            raise TypeError
        res.extend(i)
    return res
```

![](/images/lab02/flatten_1.png)
![](/images/lab02/flatten_2.png)
![](/images/lab02/flatten_3.png)
![](/images/lab02/flatten_4.png)

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

![](/images/lab02/transpose_1.png)
![](/images/lab02/transpose_2.png)
![](/images/lab02/transpose_3.png)
![](/images/lab02/transpose_4.png)
![](/images/lab02/transpose_5.png)

---

### Функция **row_sums**

Тут я снова проверил матрицу на наличие неравных строк, если они есть, функция вызывает ошибку. Потом вернул список, содержащий функцию **map** применяющюю сумирование элементов к каждой строке исходной матрицы.

```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(set(map(lambda x: len(x), mat))) > 1:
            raise ValueError
    return list(map(lambda x: sum(x), mat))
```
![](/images/lab02/row_sums_1.png)
![](/images/lab02/row_sums_2.png)
![](/images/lab02/row_sums_3.png)
![](/images/lab02/row_sums_4.png)

---

### Функция **col_sums**

Здесь с помощью условия определил "рваная" матрица или нет. И потом ко всем строкам транспонированной исходной матрицы применил функцию **sum**.

```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(set(map(lambda x: len(x), mat))) > 1:
                raise ValueError
    return [sum([mat[j][i] for j in range(len(mat))]) for i in range(len(mat[0]))]
```
![](/images/lab02/col_sums_1.png)
![](/images/lab02/col_sums_2.png)
![](/images/lab02/col_sums_3.png)
![](/images/lab02/col_sums_4.png)

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

![](/images/lab02/format_record_1.png)
![](/images/lab02/format_record_2.png)
![](/images/lab02/format_record_3.png)
![](/images/lab02/format_record_4.png)
# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике

---

## Задание A — модуль src/lab04/io_txt_csv.py

---

### Функция **read_text**

Эта функция открывает текстовый файл, читает его целиком и возвращает всё содержимое в виде одной строки (по умолчанию в кодировке UTF-8). Вместо того чтобы «падать» с ошибкой (что обычно ломает программу), она перехватывает проблемы: если файла не существует или кодировка не подходит, она просто возвращает строку с текстом ошибки («Файл не найден!» или подсказку про кодировку). Если же файл пустой, функция вернет просто пустую строку "".

```python
def read_text(path: str | Path, 
              encoding: str = "utf-8") -> str:
    
    """
    Читает текстовый файл целиком и возвращает его содержимое
    как одну строку.

    По умолчанию файл читается в кодировке UTF-8. Если нужен другой
    формат кодировки, можно передать его явно, например:
        read_text("data/input.txt", encoding="cp1251")

    Если файл не найден - функция выводит что файл не найден.
    Если кодировка не подходит к содержимому файла - аналогично
    функция напишет об этом.

    Если файл пустой - возвращается пустая строка "".
    """

    path = Path(path)
    try:
        with open(path, "r", encoding=encoding) as text:
            return text.read()
    except FileNotFoundError:
        return "Файл не найден!"
    except UnicodeDecodeError:
        return "Ошибка кодировки! Попробуйте указать encoding='utf-8'"
```

---

### Функция **write_csv**

Эта функция сохраняет переданные данные в CSV-файл: сначала она создает нужные папки, затем проверяет, чтобы все строки имели одинаковое количество колонок (и чтобы шапка header, если она есть, совпадала с ними по длине), после чего перезаписывает файл, добавляя шапку и сами данные. В блоке __main__ она просто тестируется на маленьком примере.

```python
def write_csv(rows: Iterable[Sequence], 
              path: str | Path, 
              header: tuple[str, ...] | None = None) -> None:
    ensure_parent_dir(path)

    """
    Записывает строки rows в CSV-файл path с разделителем ",".

    Если указан header - он записывается первой строкой файла.

    Файл создаётся заново (если его не было) либо полностью
    перезаписывается (если уже существовал).

    Перед записью проверяется, что все строки в rows имеют
    одинаковую длину. Если это не так - поднимается ValueError.
    Если header задан, его длина тоже должна совпадать с длиной строк.

    Если rows пуст и header=None - создаётся пустой файл (0 строк).
    Если rows пуст, а header задан - в файле будет только заголовок.
    """

    p = Path(path)
    rows = list(rows)
    row_lens = set(map(len, rows))

    if len(row_lens) != 1:
        raise ValueError("Все строки в rows должны иметь одинаковую длину")
    if header is not None and len(header) not in row_lens:
        raise ValueError("Длина header должна совпадать с длиной строк в rows")
            
    with p.open("w", newline="", encoding="utf-8") as f:
        wrt = csv.writer(f)

        if header is not None:
            wrt.writerow(header)
        for r in rows:
            wrt.writerow(r)


if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print("CSV file created.")
```

---

### Функция **ensure_parent_dir**

Эта функция берет путь к файлу и гарантирует, что все папки (включая вложенные), в которые этот файл планируется сохранить, реально существуют на диске. Если нужных директорий нет, она автоматически создаст их по цепочке (за это отвечает parents=True), а если они уже есть — просто молча продолжит работу, не выдавая ошибок (благодаря exist_ok=True).

```python
def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
```

![test1](/images/lab04/io_txt_csv_1.png)
![test2](/images/lab04/io_txt_csv_2.png)

---

## Задание B — скрипт src/lab04/text_report.py

---

### Функция **sorted_word_counts**

Эта функция берет словарь, где ключи — это слова, а значения — сколько раз они встретились (частоты), и превращает его в отсортированный список. На выходе получается список кортежей. То есть на первом месте всегда самое популярное слово, а "равные по силе" слова аккуратно выстроены по алфавиту.

```python
def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))
```

---

### Функция **main**

Код представляет собой функцию main(), которая выполняет полный цикл анализа текста: сначала читает файл (с обработкой ошибки, если файл не найден), затем очищает и разбивает текст на отдельные слова. Далее она подсчитывает общее количество слов, количество уникальных слов и частоту встречаемости каждого. Полный отсортированный список слов с частотами сохраняется в CSV-файл, а краткая статистика (всего слов, уникальных и топ-5 самых частых) выводится на экран.

```python
def main():
    try:
        raw_text = read_text(input, encoding=encode)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {input}")

    normalized_text = normalize(raw_text)
    tokenized_text = tokenize(normalized_text)
    total_words = len(tokenized_text)

    freq = count_freq(tokenized_text)
    unique_words = len(freq)

    all_rows = sorted_word_counts(freq)
    top5 = top_n(freq, n=5)

    write_csv(all_rows, output, header=("word", "count"))

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5: ")
    for word, count in top5:
        print(f"{word}: {count}")
```

![test1](/images/lab04/text_report.png)
# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)

---

## Задание A — JSON ↔ CSV

---

### Функция **json_to_csv(json_path: str, csv_path: str) -> None**

Эта функция открывает текстовый файл, читает его целиком и возвращает всё содержимое в виде одной строки (по умолчанию в кодировке UTF-8). Вместо того чтобы «падать» с ошибкой (что обычно ломает программу), она перехватывает проблемы: если файла не существует или кодировка не подходит, она просто возвращает строку с текстом ошибки («Файл не найден!» или подсказку про кодировку). Если же файл пустой, функция вернет просто пустую строку "".

```python
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте.
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError("Файл не найден")
    
    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат входного файла: ожидается .json")
    
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат выходного файла: ожидается .csv")

    with json_file.open('r', encoding='utf-8') as p:
        try:
            data = json.load(p)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой или имеет неправильный формат')
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")

    ensure_parent_dir(csv_file)

    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None

    with csv_file.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)
```

![test3](/images/lab05/json_csv_1.png)

---

### Функция **csv_to_json(csv_path: str, json_path: str) -> None**

Эта функция сохраняет переданные данные в CSV-файл: сначала она создает нужные папки, затем проверяет, чтобы все строки имели одинаковое количество колонок (и чтобы шапка header, если она есть, совпадала с ними по длине), после чего перезаписывает файл, добавляя шапку и сами данные. В блоке __main__ она просто тестируется на маленьком примере.

```python
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not csv_file.exists():
        raise FileNotFoundError("Файл не найден")
    
    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат входного файла: ожидается .json")
    
    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат выходного файла: ожидается .csv")

    
    with csv_file.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV не содержит заголовок")
        
        data = list(reader)

    if not data:
        raise ValueError("Файл CSV не содержит данных")

    ensure_parent_dir(json_file)

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
```

![test3](/images/lab05/json_csv_2.png)

---

## Задание B — CSV → XLSX

---

### Функция **csv_to_xlsx(csv_path: str, xlsx_path: str) -> None**

Код представляет собой функцию main(), которая выполняет полный цикл анализа текста: сначала читает файл (с обработкой ошибки, если файл не найден), затем очищает и разбивает текст на отдельные слова. Далее она подсчитывает общее количество слов, количество уникальных слов и частоту встречаемости каждого. Полный отсортированный список слов с частотами сохраняется в CSV-файл, а краткая статистика (всего слов, уникальных и топ-5 самых частых) выводится на экран.

```python
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использует openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    src = Path(csv_path)
    dst = Path(xlsx_path)

    if not src.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")
    if src.suffix.lower() != ".csv":
        raise ValueError(f"Неверный тип файла: ожидается .csv, получено '{src.suffix}'")
    if dst.suffix.lower() != ".xlsx":
        raise ValueError(f"Неверный тип файла: ожидается .xlsx, получено '{dst.suffix}'")

    with src.open('r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))

    if not reader:
        raise ValueError("Файл CSV пустой")

    widths = {}
    for row in reader:
        for index, cell in enumerate(row):
            if len(cell) > widths.get(index, 0):
                widths[index] = len(cell)

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in reader:
        ws.append(row)

    for index, width in widths.items():
        letter = get_column_letter(index + 1)
        ws.column_dimensions[letter].width = max(8, width)

    ensure_parent_dir(dst)
    wb.save(dst)
```

![test3](/images/lab05/cvs_xlsx.png)

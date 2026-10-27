import csv
from pathlib import Path
from typing import Iterable, Sequence


def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def read_text(path: str | Path, 
              encoding: str = "utf-8") -> str:
    
    """
    Читает текстовый файл целиком и возвращает его содержимое
    как одну строку.

    По умолчанию файл читается в кодировке UTF-8. Если нужен другой
    формат кодировки, можно передать его явно, например:
        read_text("data/input.txt", encoding="cp1251")

    Если файл не найден - функция не перехватывает ошибку,
    а даёт ей "всплыть" наружу как FileNotFoundError.
    Если кодировка не подходит к содержимому файла - аналогично
    всплывает UnicodeDecodeError.

    Если файл пустой - возвращается пустая строка "".
    """

    path = Path(path)
    try:
        with open(path, "r", encoding=encoding) as text:
            return text.read()
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден!")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Ошибка кодировки! Попробуйте указать encoding='utf-8'")


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
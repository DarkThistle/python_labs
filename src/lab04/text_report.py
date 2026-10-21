from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n

input = "data/lab04/input.txt"
output = "data/lab04/report.csv"
encode = "utf-8"


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))


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


if __name__ == "__main__":
    main()
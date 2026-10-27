import argparse
from pathlib import Path
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--in",
        dest="input_file",
        type=Path,
        required=True,
    )

    parser.add_argument(
        "--out",
        dest="output_file",
        type=Path,
        required=True,
    )

    args = parser.parse_args()

    try:
        raw_text = read_text(args.input_file, encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: файл не найден: {args.input_file}")

    norm_text = normalize(raw_text)
    token_text = tokenize(norm_text)
    word_freq = count_freq(token_text)

    words_num = len(token_text)
    unique_num = len(word_freq)
    top_5 = top_n(word_freq)

    all_rows = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))
    top_pyat = "\n".join([",".join([i[0], str(i[1])]) for i in top_5])

    write_csv(all_rows, args.output_file, header=("word", "count"))
    
    print(f"Всего слов: {words_num}\nУникальных слов: {unique_num}\nТоп-5: \n{top_pyat}")


if __name__ == "__main__":
    main()
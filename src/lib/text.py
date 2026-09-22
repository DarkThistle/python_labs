def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.replace("\\t", " ").replace("\\r", " ").replace("\\n", " ").split()

    return " ".join(text)

#print(f"Вывод: {normalize(input("Ввод: "))}")


def tokenize(text: str) -> list[str]:
    for i in range(len(text)):
        if text[i] == "-" and text[i-1].isalnum() and text[i+1].isalnum() and i not in [0, len(text)-1]:
            continue
        if text[i].isalnum():
            continue
        else:
            text = text.replace(text[i], " ")
    return text.split()

#print(f"Вывод: {tokenize(input("Ввод: "))}")

def count_freq(tokens: list[str]) -> dict[str, int]:
    tokens = dict(zip(sorted(set(tokens)), [tokens.count(i) for i in sorted(set(tokens))]))
    return tokens

#print(f"Вывод: {count_freq(eval(input("Ввод: ")))}")


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

#print(f"Вывод: {top_n(eval(input("Ввод: ")), n=2)}")

def transpose(mat: list[list[float | int]]) -> list[list]:
    trans = []
    if len(mat) == 0:
        return []
    if len(set(map(lambda x: len(x), mat))) > 1:
        raise ValueError
    return [[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]

#print(f"Вывод: {transpose(eval(input("Ввод: ")))}")


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(set(map(lambda x: len(x), mat))) > 1:
            raise ValueError
    return list(map(lambda x: sum(x), mat))

#print(f"Вывод: {row_sums(eval(input("Ввод: ")))}")


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(set(map(lambda x: len(x), mat))) > 1:
                raise ValueError
    return [sum([mat[j][i] for j in range(len(mat))]) for i in range(len(mat[0]))]

print(f"Вывод: {col_sums(eval(input("Ввод: ")))}")
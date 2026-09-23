def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    return min(nums), max(nums)

#print(f"Вывод: {min_max(eval(input("Ввод: ")))}")


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

#print(f"Вывод: {unique_sorted(eval(input("Ввод: ")))}")


def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if type(i) is not list and type(i) is not tuple:
            raise TypeError
        res.extend(i)
    return res

print(f"Вывод: {flatten(eval(input("Ввод: ")))}")


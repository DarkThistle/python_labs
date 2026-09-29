def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    mini = nums[0]
    maxi = nums[0]
    for i in nums:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    return mini, maxi
    
print(f"Вывод: {min_max(eval(input("Ввод: ")))}")


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums = list(set(nums))
    res = [nums[0]]
    while not(all([nums[i] <= nums[i+1] for i in range(len(nums) - 1)])):
        for k in range(len(nums)-1):
            if nums[k] > nums[k+1]:
                nums[k], nums[k+1] = nums[k+1], nums[k]
    return sorted(set(nums))

print(f"Вывод: {unique_sorted(eval(input("Ввод: ")))}")


def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if type(i) is not list and type(i) is not tuple:
            raise TypeError
        res.extend(i)
    return res

#print(f"Вывод: {flatten(eval(input("Ввод: ")))}")


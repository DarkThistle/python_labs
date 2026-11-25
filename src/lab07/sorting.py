def bubble_sort(nums):
    """
    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    copie = nums.copy()
    flag = False
    n = len(nums)
    while flag == False:
        c = 0
        for i in range(n-1):
            if copie[i] > copie[i+1]:
                c += 1
                copie[i], copie[i+1] = copie[i+1], copie[i]
        if c == 0:
            flag = True
    return copie


def insertion_sort(nums):
    copie = nums.copy()
    for i in range(len(copie)-1):
        for j in range(i, -1, -1):
            if copie[j+1] < copie[j]:
                copie[j+1], copie[j] = copie[j], copie[j+1]
            else:
                break
    return copie

 
def selection_sort(nums):
    copie = nums.copy()
    n = len(copie)
    c = 0
    for i in range(c, n):
        mini = i
        for j in range(i+1, n):
            if copie[j] <= copie[mini]:
                mini = j
        copie[mini], copie[i] = copie[i], copie[mini]
        c+= 1
    return copie
        




if __name__ == "__main__":
    print(bubble_sort([232, 1, 2, 5, 7, 32, 8, 9, 1]))
    print(insertion_sort([232, 1, 2, 5, 7, 32, 8, 9, 1]))
    print(selection_sort([232, 1, 2, 5, 7, 32, 8, 9, 1]))
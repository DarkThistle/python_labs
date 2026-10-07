def transpose(mat: list[list[float | int]]) -> list[list]:
    trans = []
    if len(mat) == 0:
        return []
    if len(set(map(lambda x: len(x), mat))) > 1:
        raise ValueError
    return [[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]

print(transpose([[1, 2, 3]]))    
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))  
print(transpose([])) 
print(transpose([[1, 2], [3]]))


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(set(map(lambda x: len(x), mat))) > 1:
            raise ValueError
    return list(map(lambda x: sum(x), mat))

print(row_sums([[1, 2, 3], [4, 5, 6]]))   
print(row_sums([[-1, 1], [10, -10]]))  
print(row_sums([[0, 0], [0, 0]]))     
print(row_sums([[1, 2], [3]]))   


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(set(map(lambda x: len(x), mat))) > 1:
                raise ValueError
    return [sum([mat[j][i] for j in range(len(mat))]) for i in range(len(mat[0]))]

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))  
print(col_sums([[0, 0], [0, 0]]))     
print(col_sums([[1, 2], [3]]))    
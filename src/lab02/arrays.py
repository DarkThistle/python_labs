def min_max(num_list):
    num_list = num_list.strip("[]").split(", ")
    if "" not in num_list:
        num_list = list(map(lambda x: float(x) if "." in x else int(x), num_list))
        return (min(num_list)), max(num_list)
    return "ValueError"


def unique_sorted(num_list):
    num_list = num_list.strip("[]").split(", ")
    if "" not in num_list:
        num_list = sorted(list(set(list(map(lambda x: float(x) if "." in x else int(x), num_list)))))
        return num_list
    else: 
        return []

def flatten(num_list):
    num_list = [[int(j) for j in i[i.find("[")+1:i.find("]")].split(", ")] for i in num_list[1:-1].replace("(", "[").replace(")", "]").replace("], [", "].[").split(".")]
    new_list = []
    for i in num_list:
        new_list += i
    return new_list


#print(min_max(input()))
print(flatten(input()))

# [3, -1, 5, 5, 0]
# [-5, -2, -9] 
# [42]
# []
# [1.5, 2, 2.0, -3.1]

#print(input().strip("[]").split(", "))
#print(max(["2.0", "2"]))
#print(int(2.9))


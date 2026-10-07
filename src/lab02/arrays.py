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
    
print(min_max([3, -1, 5, 5, 0]))    
print(min_max([42]))                 
print(min_max([-5, -2, -9]))          
print(min_max([1.5, 2, 2.0, -3.1]))   
print(min_max([])) 


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums = list(set(nums))
    res = [nums[0]]
    while not(all([nums[i] <= nums[i+1] for i in range(len(nums) - 1)])):
        for k in range(len(nums)-1):
            if nums[k] > nums[k+1]:
                nums[k], nums[k+1] = nums[k+1], nums[k]
    return nums

print(unique_sorted([3, 1, 2, 1, 3]))       
print(unique_sorted([]))                      
print(unique_sorted([-1, -1, 0, 2, 2]))        
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))  


def flatten(mat: list[list | tuple]) -> list:
    res = []
    for i in mat:
        if type(i) is not list and type(i) is not tuple:
            raise TypeError
        res.extend(i)
    return res

print(flatten([[1, 2], [3, 4]]))       
print(flatten([[1, 2], (3, 4, 5)]))    
print(flatten([[1], [], [2, 3]]))    
print(flatten([[1,2], 'ab']))  

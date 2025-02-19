def two_sum(nums, target):
    sol={}
    for i,num in enumerate(nums):
        compliment = target - num
        if compliment in sol:
            return [sol[compliment], i]
        
        sol[num] = i
    return "No Matches Found"

nums = [11, 2, 15, 77]
target = 9

print(two_sum(nums, target))


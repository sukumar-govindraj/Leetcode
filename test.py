
def two_sum(nums, target):
    hash_set={}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_set:
            return [hash_set[complement], i]
        hash_set[complement] = i



nums = [2, 7, 11, 15]
target = 9


print(two_sum(nums, target)  )
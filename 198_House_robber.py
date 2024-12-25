def rob_house(nums, i=None, memo=None):

    if memo is None:
        memo={}

    if i is None:
        i=len(nums)-1

    if i<0:
        return 0
    
    if i in memo:
        return memo[i]
    
    memo[i]= max(rob_house(nums, i-1, memo), nums[i]+rob_house(nums, i-2, memo))

    return memo[i]

nums1=[2,7,9,3,1]
print(rob_house(nums1))

nums2 = [1,2,3,1]
print(rob_house(nums2))
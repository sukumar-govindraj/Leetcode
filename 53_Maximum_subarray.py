def max_sub_array(nums):

    max_sum=nums[0]
    current_sum=nums[0]

    for i in range(1, len(nums)):
        current_sum = max(current_sum + nums[i], nums[i])
        max_sum = max(current_sum, max_sum)

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]

print(max_sub_array(nums))



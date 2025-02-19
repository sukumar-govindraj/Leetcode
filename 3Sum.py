def Three_sum(nums):
    res=[]
    for i in range(len(nums)):

        left, right = 0, len(nums)-1

        if (i+ nums[left] + nums[right]) == 0:
            res.append([i, left, right])

        while (left < right):
            if nums[left] == nums[right]:
                left+=1
                right-=1







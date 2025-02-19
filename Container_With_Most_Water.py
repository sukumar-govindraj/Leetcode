def Container_With_Most_Water(nums):

    left, right = 0, len(nums)-1
    max_area=0
    start, end=0,0
    while (left<right):

        current_area = (right -left) * (min(nums[left], nums[right]))

        if current_area > max_area:
            max_area = current_area
            start, end = left, right

        if nums[left] > nums[right]:
            right-=1
        else:
            left+=1
    
    return max_area, start, end


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Container_With_Most_Water(height)) 


        



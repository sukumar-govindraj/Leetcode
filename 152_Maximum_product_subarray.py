# def max_product_sub_array(nums):

#     max_product=nums[0]
#     current_prod=nums[0]


#     for i in range(1, range(len(nums))):

#         current_prod =  max(current_prod * nums[i], nums[i])


# Build the recurssion condition for every next stage 
# then decide what u want to do with the resukt of each recurssion result
# 

def sum_of_digits(n):

    if n==0: 
        return 0
    
    res=n%10

    sum =  sum_of_digits(n//10) + res

    return sum


print(sum_of_digits(123))
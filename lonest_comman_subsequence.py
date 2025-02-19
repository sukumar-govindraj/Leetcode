# def lcm(a, b):

#     if a == '' or b == '':
#         return 0

#     if(a[-1] == b[-1]):
#         res = 1+ lcm(a[:-1], b[-1])
#     else:
#         res = max(lcm(a[:-1], b) , lcm(a, b[:-1]))

#     return res

# print(lcm("abcde","ace"))





# def sun_seq_ret(a,i=None,res=None):
#     if i is None:
#         i=0
    
#     if res is None:
#         res=[]

#     if i == len(a):
#         ans=[]
#         return ans+res
    
#     res1 = sun_seq_ret(a,i+1, res+[a[i]])
#     res2 = sun_seq_ret(a,i+1, res)

#     return res1+res2

# print(sun_seq_ret('abc'))


def sub_seq(text):
    # Base Case: When the string is empty
    if text == '':
        return ['']  # Return a list with an empty subsequence

    # Recursive Case: Exclude and Include the last character
    exclude = sub_seq(text[:-1])# Subsequences without the last character
    include = [sub + text[-1] for sub in exclude]  # Add the last character to each subsequence

    # Combine the results
    return exclude + include

# Example Usage
print(sub_seq('abc'))


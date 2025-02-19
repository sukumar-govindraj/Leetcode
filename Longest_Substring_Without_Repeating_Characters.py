# def LSWRC(string):
#     start=0
#     sol={}
#     count=0
#     sol_str_start, sol_str_end = 0,0
#     for i, s in enumerate(string):
#         if s in sol:
#             start = sol[s] + 1
#         sol[s] = i

#         if count < (sol[s] - start+1):
#             count = sol[s] - start+1
#             sol_str_start, sol_str_end = start, sol[s]

#         # count = max(count, sol[s] - start+1)
#     return string[sol_str_start: sol_str_end +1]




# string = 'aabcdabcdegfccde'

# print(LSWRC(string))


def length_of_longest_substring(s):
    char_map = {}  # To store the last seen position of each character
    left = 0  # Left pointer for the sliding window
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)  # Move left to avoid repetition
        
        char_map[s[right]] = right  # Update the last seen position of the character
        max_length = max(max_length, right - left + 1)  # Calculate the current window size
    
    return max_length

# Example usage:
s = "aabcdabcdegfccde"
print(length_of_longest_substring(s))  # Output: 3
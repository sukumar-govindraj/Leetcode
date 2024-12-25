def climb_stairs(n, memo={}):

    if n in memo:
        return memo[n]
    
    if n==1 or n==2:
        return n
    
    memo[n] = climb_stairs(n-1, memo) + climb_stairs(n-2, memo)

    return memo[n]


result = climb_stairs(4)
print(result)


def min_steps(n, memo=None):

    if memo is None:
        memo={}

    if n in memo:
        return memo[n]
    
    if n==1 or n==2:
        return 1
    
    memo[n] = 1 + min(min_steps(n-1, memo), min_steps(n-2, memo))

    return memo[n]


print(min_steps(15))
    











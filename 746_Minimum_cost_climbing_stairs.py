def min_cost(cost, i=None, memo=None):

    if memo is None:
        memo ={}

    if i is None:
        i=len(cost)

    if i in memo:
        return memo[i]
    
    if i <= 1:
        return 0

    min_price= min(min_cost(cost, i-1, memo)+cost[i-1], min_cost(cost, i-2, memo)+cost[i-2])

    return min_price
    

cost = [10, 15, 20]
print(min_cost(cost))
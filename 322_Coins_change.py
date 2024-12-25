def coin_change(coins, amount, memo= None):

    min_coins=float('inf')

    if memo is None:
        memo={}
    if amount in memo:
        return memo[amount]
    if amount < 0: 
        return float("inf")
    
    if amount==0:
        return 0
    
    for coin in coins:
        result = coin_change(coins, amount-coin, memo)
        min_coins = min(min_coins, result+1)

    return min_coins


coins = [2]
amount=3
result=coin_change(coins, amount)
print(result)

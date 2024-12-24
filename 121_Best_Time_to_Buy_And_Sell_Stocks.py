
class Solution:

    def max_profit(self, prices: List[int]) -> int:
        left, right = 0,1
        max_profit= 0 

        while right<len(prices):
            if (prices[left] < prices[right]):
                profit = prices[left] - prices[right]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right+=1


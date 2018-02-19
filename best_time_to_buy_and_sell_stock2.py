"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        
        if len(prices) == 0:
            return 0
        
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        
        while i < (len(prices) - 1):
            while i < (len(prices) - 1) and (prices[i] >= prices[i + 1]):
                i += 1
            valley = prices[i]
            while i < (len(prices) - 1) and (prices[i] <= prices[i + 1]):
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        
        return maxprofit 



s = Solution()
sol = s.maxProfit([7, 1, 5, 3, 6, 4])
if sol:
    print ("Maximum profit could be {} ".format(sol))


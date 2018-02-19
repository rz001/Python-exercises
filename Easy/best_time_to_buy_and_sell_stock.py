"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""
import sys 

class Solution(object):
    def maxProfit(self, prices):
        minprice = sys.maxint
        maxprofit = 0
        for i in range(0, len(prices)): 
            if (prices[i] < minprice):
                minprice = prices[i]
            elif (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice
        
        return maxprofit
    

"""
Brute force - time limit exeeded - not accepted by leetcode
class Solution(object):
    def maxProfit(self, prices):
        
        :type prices: List[int]
        :rtype: int
        
        sellp = 0
        buyp = 0
        maxprofit = 0
        for i in range(0, len(prices)):
            for x in range(i+1, len(prices)):
                sellp = prices[i] - prices[x]
                buyp = prices[x] - prices[i]
                if maxprofit < max(sellp, buyp) and prices[x] > prices[i]:
                    maxprofit = max(sellp, buyp)

        return maxprofit
"""

s = Solution()
sol = s.maxProfit([7, 1, 5, 3, 6, 4])
if sol:
    print ("Maximum profit could be {} ".format(sol))


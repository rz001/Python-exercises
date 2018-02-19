"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Input:4
Output:5
1. s1, s1, s1, s1 (n)
2. s2, s2 (n/2)
3. s2, s1, s1 (n/2 +2)
4. s1, s1, s2 (2 + n/2)
5. s1, s2, s1 (1 + n/2 + 1)
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb_Stairs(i, n, memo):
            if (i > n):
                return 0
            if (i == n):
                return 1
            if (memo[i] > 0):
                return memo[i]
        
            memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo)
            return memo[i]

        memo = [None] * (n + 1)
        return climb_Stairs(0, n, memo)

    	
  
s = Solution()
res = s.climbStairs(4)
print ("There are {} ways to the top".format(res))

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
    
        if (n == 1):
            return "1"
        if (n == 2): 
            return "11"

        outs = "11"
        for i in range(3, n+1):
       
            outs += 'a'
            lout = len(outs) 
            cnt = 1 
            tmp = '' 
        
            for j in range(1, lout):
                if (outs[j] != outs[j-1]):
                    tmp += str(cnt) 
                    tmp += outs[j-1]
                    cnt = 1
                else:
                     cnt += 1 
            outs = tmp
    
        return outs    
        

sl = Solution()
res = sl.countAndSay(6)

if res:
    print ("Nth term of the count-and-say sequence is {}".format(res))

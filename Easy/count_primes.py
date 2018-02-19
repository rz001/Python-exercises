"""
Description:

Count the number of prime numbers less than a non-negative number, n.
Let's start with a isPrime function. To determine if a number is prime, we need to check if it is not divisible by any number less than n. 
The runtime complexity of isPrime function would be O(n) and hence counting the total prime numbers up to n would be O(n2). Could we do better?
"""

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in xrange(2, n):
            if res[i] == True:
                for j in xrange(i, (n-1)/i+1):
                    res[i*j] = False
        return sum(res)
"""

import math 

class Solution(object):
    def countPrimes(self, n):
    
        #:type n: int
        #:rtype: int
    
   
        def isPrime(x): 
            for j in range(x, (n-1)/x + 1):
                if x % j == 0:
                    return False
            return True
        
        nprimes = 0
       
        for i in range(2, n):
            if isPrime(i):
                nprimes += 1
        
        return nprimes
"""      

s = Solution()
sol = s.countPrimes(10)
if sol != None:
    print ("The number of primes is {}".format(sol))      
        

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i = len(a) - 1
        x = len(b) - 1 

        t = max(i,x)

        if i < x:
            for d in range(0, x-i):
                a = '0' + a     
        elif i > x:
            for d in range(0, i-x):
                b = '0' + b
        
        sumn = []
        carry = 0
       
        while t >= 0:

            if int(a[t]) ^ int(b[t]):
                if carry == 1:
                    sumn.insert(0,'0')
                else:
                    sumn.insert(0, '1')
                    carry = 0     
            elif int(a[t]) and int(b[t]):
                if carry == 1:
                    sumn.insert(0,'1')
                else:
                    sumn.insert(0,'0')
                    carry = 1
            elif carry == 1:
                sumn.insert(0,'1')
                carry = 0
            else:
                sumn.insert(0,'0')

            t -= 1
         
        
        if carry == 1:
            sumn.insert(0,'1')

        return ''.join(sumn)

s = Solution()
sol = s.addBinary('1010','1011')
if sol != None:
    print ("Sum is {}".format(sol))
class Solution:
    def sumOfDigits(self, n):
        if n//10==0:
            return n
        else:
            temp = self.sumOfDigits(n//10)
            return temp+n%10

class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7:
            return True
        elif n<10:
            return False
        tot=0
        while n!=0:
            tot+=(n%10)*(n%10)
            n=n//10
        return self.isHappy(tot)
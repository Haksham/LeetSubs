class Solution:
    def totalMoney(self, n: int) -> int:
        w=n//7
        e=n%7
        return 28*w+7*(w-1)*w//2 + e*w+e*(e+1)//2
class Solution:
    def smallestNumber(self, n: int) -> int:
        if n==1:
            return 1
        for i in range(1,n):
            if (2**i)-1 >=n:
                return (2**i)-1
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i=0
        ls=[]
        while(n>=3**i):
            ls.append(3**i)
            i+=1
        for i in range(len(ls)-1,-1,-1):
            if n==0:
                return True
            if ls[i]<=n and n-ls[i]>=0:
                n-=ls[i]
                if n==0:
                    return True
        return False
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i=0
        ls=[]
        while(n>=3**i):
            ls.append(3**i)
            i+=1
        print(ls)
        t=n
        for i in range(len(ls)-1,-1,-1):
            if t==0:
                return True
            if ls[i]<=n:
                if t-ls[i]>=0:
                    t=t-ls[i]
                    if t==0:
                        return True
            print(t,ls[i])
        return False
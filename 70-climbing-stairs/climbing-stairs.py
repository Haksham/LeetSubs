class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        fac=[1]
        for i in range(1,n+1):
            fac.append(fac[i-1]*i)
        sm=0
        if n%2==0:
            rg=(n-1)//2+1
        else:
            rg=n//2+1
        print(fac,rg)
        for i in range(rg+1):
            print(fac[n-i],fac[n-i*2],fac[i])
            sm+=fac[n-i]//(fac[n-i*2]*fac[i])
        return sm
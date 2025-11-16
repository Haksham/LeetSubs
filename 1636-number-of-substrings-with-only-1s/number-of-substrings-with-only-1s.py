class Solution:
    def numSub(self, s: str) -> int:
        p=0
        ans=0
        mod = int(10 ** 9 + 7)
        for i in s:
            if i=="1":
                p+=1
            elif i=="0" and p:
                ans+=((p*(p+1))//2)%mod
                p=0
        if p:
            ans+=((p*(p+1))//2)%mod
        return ans
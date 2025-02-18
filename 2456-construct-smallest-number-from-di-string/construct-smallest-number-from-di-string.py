class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n=len(pattern)
        ans=[]
        ans.append(1)
        p=0
        for i in range(n):
            if pattern[i]=="I":
                ans.append(i+2)
                p=i+1
            elif pattern[i]=="D":
                ans.insert(p,i+2)
        res=""
        for i in ans:
            res+=str(i)
        return res
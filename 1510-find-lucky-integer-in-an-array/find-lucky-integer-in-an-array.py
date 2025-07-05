class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic={}
        ans=-1
        for i in arr:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        k=list(dic.keys())
        v=list(dic.values())
        for i in range(len(k)-1,-1,-1):
            if k[i]==v[i] and ans<k[i]:
                ans=k[i]
        return ans
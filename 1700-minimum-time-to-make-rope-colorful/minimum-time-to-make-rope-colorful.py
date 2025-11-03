class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev=0
        tot=0
        arr=[]
        for i in range(len(colors)):
            if prev==colors[i]:
                arr.append(neededTime[i])
            elif prev!=colors[i]:
                if len(arr)!=0:
                    tot+=sum(arr)-max(arr)
                arr=[]
                arr.append(neededTime[i])
            prev=colors[i]
        if len(arr)>1:
            tot+=sum(arr)-max(arr)
        return tot
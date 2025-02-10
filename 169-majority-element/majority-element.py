from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        mx=max(dic,key=dic.get)
        return mx
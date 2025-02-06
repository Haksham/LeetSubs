from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        dic=defaultdict(int)
        for i in range(n):
            for j in range(i+1,n):
                product=nums[i]*nums[j]
                c+=dic[product]
                dic[product]+=1
        print(dic)
        return c*8
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        p=0
        ls=[]
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                p+=1
            elif nums[i]!=0 and p!=0:
                ls.append(p)
                p=0
        if p!=0:
            ls.append(p)
        for i in ls:
            res+=(i*(i+1))//2
        return res
            
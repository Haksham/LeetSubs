class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sm=sum(nums)
        c=0
        while sm%k!=0:
            c+=1
            sm-=1
        return c
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=float('-inf')
        curr=0
        for i in nums:
            curr+=i
            if curr>mx:
                mx=curr
            if curr<0:
                curr=0
        return mx
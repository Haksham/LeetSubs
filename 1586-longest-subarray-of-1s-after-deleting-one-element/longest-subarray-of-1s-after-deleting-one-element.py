class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, c, res = 0, 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            
            while c > 1:
                if nums[left] == 0:
                    c -= 1
                left += 1
            
            res = max(res, i - left)
        
        return res
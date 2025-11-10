class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = [0] * (len(nums) + 1)
        top = 0
        ans = 0

        for i in nums:
            while stack[top] > i:
                top -= 1
                ans += 1
            if stack[top] != i:
                top += 1
                stack[top] = i

        return ans + top
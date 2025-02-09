from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counter = Counter()
        c = 0
        for i, x in enumerate(nums):
            c += i-counter[i-x]
            counter[i-x]+= 1
        return c
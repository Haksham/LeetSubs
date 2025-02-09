from collections import Counter
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        c = 0 
        n = len(nums)
        new = [ num - index for index, num in enumerate(nums)]
        c = Counter(new)
        tot = n*(n-1)/2 
        print(new,c)
        for key, val in c.items(): 
            if val!=1:
                tot -= val*(val-1)/2
        return int(tot)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ch=set()
        for i in range(len(nums)):
            if nums[i] in ch:
                return True
            ch.add(nums[i])
            if len(ch)>k:
                ch.remove(nums[i-k])
        return False
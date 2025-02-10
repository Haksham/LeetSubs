class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=1
        n=len(nums)
        prev=nums[0]
        for i in range(1,n):
            if nums[i]!=prev:
                nums[counter]=nums[i]
                counter+=1
                prev=nums[i]
        return counter
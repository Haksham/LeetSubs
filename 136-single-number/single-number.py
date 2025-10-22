class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=set()
        arr=[]
        ans=0
        for i in nums:
            if i not in c:
                c.add(i)
                arr.append(i)
            elif i in c:
                arr.remove(i)
        return arr[0]
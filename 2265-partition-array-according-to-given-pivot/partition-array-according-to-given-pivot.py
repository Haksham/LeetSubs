class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        r=[]
        m=[]
        for i in nums:
            if i==pivot:
                m.append(i)
            elif i>pivot:
                r.append(i)
            elif i<pivot:
                l.append(i)
        return l+m+r
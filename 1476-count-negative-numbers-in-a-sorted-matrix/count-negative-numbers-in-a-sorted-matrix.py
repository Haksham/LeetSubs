class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in grid:
            for j in reversed(i):
                if j<0:c+=1
                elif j>=0:break
        return c
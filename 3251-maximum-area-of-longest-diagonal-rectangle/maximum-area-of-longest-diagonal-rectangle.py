import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mx=0
        area=0
        for i in dimensions:
            if mx<i[0]*i[0]+i[1]*i[1]:
                mx=i[0]*i[0]+i[1]*i[1]
                area=i[0]*i[1]
                print(mx, area, i)
            elif mx==i[0]*i[0]+i[1]*i[1]:
                area=max(area,i[0]*i[1])
                print(mx, area, i)
        return area
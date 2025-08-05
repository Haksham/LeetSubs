class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        f=[0]*len(fruits)
        b=[0]*len(baskets)
        c=len(fruits)
        j=0

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j] and b[j]!=1:
                    b[j]=1
                    c-=1
                    break
        return c
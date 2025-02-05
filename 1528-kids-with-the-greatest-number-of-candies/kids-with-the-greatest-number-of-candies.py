class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx=max(candies)
        ls=[False for _ in candies]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=mx:
                ls[i]=True
        return ls
        
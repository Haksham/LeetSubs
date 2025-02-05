class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        l=0
        n=len(prices)
        r=1
        while r<n:
            if prices[r]>prices[l]:
                mx=max(prices[r]-prices[l],mx)
            else:
                l=r
            r+=1
        return mx
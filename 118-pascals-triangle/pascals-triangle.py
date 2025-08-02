class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[]]*numRows
        if numRows==0:
            return [[]]
        for i in range(numRows):
            ans[i]=[1]*(i+1)
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return (ans)
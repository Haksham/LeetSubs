class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        ls=[[] for _ in range(2*n-1)]
        ans=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ls[n-i+j-1].append(grid[i][j])
        for i in range(len(ls)):
            if i<n:
                ls[i].sort(reverse=True)
            else:
                ls[i].sort()
        for i in range(len(ls)):
            for j in range(len(ls[i])):
                if i>=n:
                    ans[j].append(ls[i][j])
                else:
                    ans[n-i+j-1].append(ls[i][j])
                print(i,j,ls[i],ans)
        return (ans)
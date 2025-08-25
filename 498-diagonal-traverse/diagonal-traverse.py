class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n=len(mat[0])+len(mat)-1
        ans=[[] for i in range(n)]
        c=0
        for x,i in enumerate(mat):
            for j in range(len(i)):
                ans[j+c+x].append(i[j])
            c+1
        for x,i in enumerate(ans):
            if x%2==0:
                i=i.reverse()
        res=[]
        for i in ans:
            for j in i:
                res.append(j)
        return res
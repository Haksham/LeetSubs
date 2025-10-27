class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        oldC=0
        tot=0
        for i in bank:
            t=0
            for j in i:
                if j=='1':t+=1
            if t!=0:
                tot+=t*oldC
                oldC=t
            # print(t,tot,oldC)
        return tot
            
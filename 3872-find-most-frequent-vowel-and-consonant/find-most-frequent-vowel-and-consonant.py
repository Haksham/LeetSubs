class Solution:
    def maxFreqSum(self, s: str) -> int:
        dv={"a":0,"e":0,"i":0,"o":0,"u":0}
        dc={}
        for i in s:
            if i in dv.keys():
                dv[i]+=1
            elif i in dc.keys():
                dc[i]+=1
            else:
                dc[i]=1
        v1=list(dv.values())
        v2=list(dc.values())
        print(dv,dc)
        if len(v1)==0 and len(v2==0):
            return 0
        elif len(v1)==0:
            return max(v2)
        elif len(v2)==0:
            return max(v1)
        else:
            return max(v1)+max(v2)
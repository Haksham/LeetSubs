class Solution:
    def romanToInt(self, s: str) -> int:
        dic={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        tot=0
        n=len(s)
        for x in range(n):
            if x<n-1 and dic[s[x]]<dic[s[x+1]]:
                tot-=dic[s[x]]
            else:
                tot+=dic[s[x]]
        return tot
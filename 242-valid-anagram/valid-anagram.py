from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1=len(s)
        n2=len(t)
        if n1!=n2:
            return False
        dic1=defaultdict(int)
        dic2=defaultdict(int)
        for i in range(n1):
            dic1[s[i]]+=1
        for j in range(n2):
            dic2[t[j]]+=1
        
        if dic1!=dic2:
            return False
        else:
            return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p=0
        for i in range(len(t)):
            if p==len(s):
                break
            if s[p]==t[i]:
                p+=1
        if p==len(s):
            return True
        else: return False
class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split(" ")
        st=" ".join([st[i] for i in range(len(st)-1,-1,-1) if len(st[i])>0])
        return st
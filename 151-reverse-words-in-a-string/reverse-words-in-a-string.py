class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split(" ")
        n=len(st)
        st=[st[i] for i in range(n-1,-1,-1) if len(st[i])>0]
        st=" ".join(st)
        return st
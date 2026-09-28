class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=0
        mx=0
        for i in range(len(s)):
            if s[i]=="(":
                x+=1
            elif s[i]==")":
                x-=1
            if mx<x:
                mx=x
        return mx
        
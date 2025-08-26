class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        dic={}
        if len(s)<k:
            return 0
        for i in s:
            dic[i]=dic.get(i,0)+1
        for i ,ch in enumerate(s):
            if dic[ch]<k:
                left=self.longestSubstring(s[:i],k)
                right=self.longestSubstring(s[i+1:],k)
                return max(left,right)
        return len(s)

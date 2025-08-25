class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch=set()
        l=0
        mx=0
        for i in range(len(s)):
            while s[i] in ch:
                ch.remove(s[l])
                l+=1
            ch.add(s[i])
            mx=max(mx,i-l+1)
        return mx
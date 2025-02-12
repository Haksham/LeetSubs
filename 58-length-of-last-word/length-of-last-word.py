class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=s.split(" ")
        x=[i for i in x if len(i)>0]
        print(x)
        return len(x[-1])
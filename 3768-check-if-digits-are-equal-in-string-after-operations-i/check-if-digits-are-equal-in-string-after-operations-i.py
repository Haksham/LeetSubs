class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(1):
            if len(s)==2:
                if s[0]==s[1]:
                    return True
                else:
                    return False
            t=""
            for i in range(len(s)-1):
                t+=str((int(s[i])+int(s[i+1]))%10)
            s=t
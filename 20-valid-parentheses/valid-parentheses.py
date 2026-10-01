class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        a=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                a.append(i)
            elif i==")":
                if len(a)>0 and a[-1]=="(":
                    a.pop()
                else:
                    return False
            elif i=="]":
                if len(a)>0 and a[-1]=="[":
                    a.pop()
                else:
                    return False
            elif i=="}":
                if len(a)>0 and a[-1]=="{":
                    a.pop()
                else:
                    return False
        if len(a)==0: return True
        else: return False
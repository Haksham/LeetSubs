class Solution:
    def clearDigits(self, s: str) -> str:
        stk=[]
        for i in s:
            if i.isalpha():
                stk.append(i)
            if i.isdigit():
                stk.pop()
        stk="".join(stk)
        return stk
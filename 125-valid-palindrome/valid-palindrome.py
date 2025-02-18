class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalpha():
                a+=i.lower()
            elif i.isdigit():
                a+=i
        f=0
        n=len(a)
        for i in range(n//2):
            if a[i]!=a[n-1-i]:
                f=1
        if f==1:
            return False
        else:
            return True
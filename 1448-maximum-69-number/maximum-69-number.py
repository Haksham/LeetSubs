class Solution:
    def maximum69Number (self, num: int) -> int:
        st=[i for i in str(num)]
        for i in range(len(st)):
            if st[i]=="6":
                st[i]="9"
                break
        return int("".join(st))

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()     
        curr = set()   

        for num in arr:
            new_curr = {num}
            for prev in curr:
                new_curr.add(prev | num)  
            curr = new_curr
            res |= curr 

        return len(res)
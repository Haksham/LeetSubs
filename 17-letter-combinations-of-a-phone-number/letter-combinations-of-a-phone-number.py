class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic= {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        ans=[]
        if not digits:
            return []
        def back(i,x):
            if i==len(digits):
                ans.append("".join(x))
                return 
            letters=dic[digits[i]]
            for j in letters:
                x.append(j)
                back(i+1,x)
                x.pop()
        back(0,[])
        return ans

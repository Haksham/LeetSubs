class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            ls=[j for j in i]
            ls.sort()
            if "".join(ls) not in dic:
                dic.update({"".join(ls):[i]})
            else:
                dic["".join(ls)].append(i)
        
        ans=[]
        for i in dic.keys():
            ans.append(dic[i])
        return(ans[::-1])
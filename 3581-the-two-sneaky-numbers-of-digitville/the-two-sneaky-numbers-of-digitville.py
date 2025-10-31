class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        st=set()
        i=0
        while len(ans)<2:
            if nums[i] in st:
                ans.append(nums[i])
            else:
                st.add(nums[i])
            # print(ans,st)
            i+=1
        return ans
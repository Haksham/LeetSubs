class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans=0
        for i in range(len(energy)):
            if initialEnergy<=energy[i]:
                ans+=energy[i]-initialEnergy+1
                initialEnergy+=energy[i]-initialEnergy+1
            if initialExperience<=experience[i]:
                ans+=experience[i]-initialExperience+1
                initialExperience+=experience[i]-initialExperience+1

            initialEnergy-=energy[i]
            initialExperience+=experience[i]
            print(ans)
        return ans
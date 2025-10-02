class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full=numBottles
        empty=0
        ex=numExchange
        drunk=numBottles
        while full+empty>=ex:
            empty+=full
            full=0
            if empty>=ex:
                empty-=ex
                ex+=1
                full+=1
            else:
                break
            drunk+=full
        return drunk
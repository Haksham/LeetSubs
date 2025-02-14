class ProductOfNumbers:
    ls=[]
    def __init__(self):
        self.ls.append(1)

    def add(self, num: int) -> None:
        if num==0:
            self.ls=[]  
            self.ls.append(1)
        else:
            self.ls.append(self.ls[-1]*num)

    def getProduct(self, k: int) -> int:
        if k>len(self.ls)-1:
            return 0
        else:
            return self.ls[-1]//self.ls[-1-k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
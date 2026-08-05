class Solution:
    def choose(self,a,b):
        product = 1
        product2 = 1
        for i in range(b):
            product*=a-i
        for j in range(b):
            product2*=(j+1)
        return int(product/product2)
    def uniquePaths(self, m: int, n: int) -> int:
        ans = self.choose(m+n-2,n-1)
        return ans
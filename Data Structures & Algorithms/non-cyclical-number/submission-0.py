class Solution:
    def sumSquares(self,n):
        total = 0
        while (n>0):
            total+=(n%10)*(n%10)
            n = n//10
        return total
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n
        while curr not in seen:
            seen.add(curr)
            curr = self.sumSquares(curr)
        if curr == 1:
            return True
        return False
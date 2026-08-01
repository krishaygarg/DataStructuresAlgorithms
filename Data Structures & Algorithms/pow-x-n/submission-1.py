class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        curr = x
        if n>0:
            for i in range(32):
                if i>0:
                    curr = curr*curr
                if (n%2==1):
                    ans*=curr
                n = n//2
        else:
            n = ~n+1
            for i in range(32): 
                if i>0:
                    curr = curr*curr
                if (n%2==1):
                    ans/=curr
                n = n//2
        return ans

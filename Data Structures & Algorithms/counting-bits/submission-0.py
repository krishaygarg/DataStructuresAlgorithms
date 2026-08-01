class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        curPos = 0
        endPos = 0
        for i in range(1,n+1):
            ans[i] = ans[curPos]+1
            curPos+=1
            if curPos > endPos:
                curPos = 0
                endPos = i
        return ans
        
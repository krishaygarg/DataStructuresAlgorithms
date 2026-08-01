class Solution:
    def expand(self, s, l, r):
        if s[l]!=s[r]:
            return 0, l, r
        while (l>0 and r<len(s)-1):
            if s[l-1]==s[r+1]:
                l-=1
                r+=1
            else:
                break
        return r-l+1, l, r
    def longestPalindrome(self, s: str) -> str:
        bestLen = 0
        bestStr = ""
        for i in range(len(s)):
            length, l, r = self.expand(s,i,i)
            # print(length)
            if length>bestLen:
                bestLen = length
                bestStr = s[l:r+1]
            if i<len(s)-1:
                length,l,r = self.expand(s,i,i+1)
                if length>bestLen:
                    bestLen = length
                    bestStr = s[l:r+1]
        print(bestLen)
        return bestStr

        
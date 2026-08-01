class Solution:
    def expand(self, s, l, r):
        if s[l]!=s[r]:
            return 0
        count = 1
        while (l>0 and r<len(s)-1):
            if s[l-1]==s[r+1]:
                l-=1
                r+=1
                count+=1
            else:
                break
        return count
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count+=self.expand(s,i,i)
        for i in range(len(s)-1):
            count+=self.expand(s,i,i+1)
        return count
from collections import defaultdict
class Solution:
    def check(self,freq_s,freq_t):
        for key,value in freq_t.items():
            if freq_s[key]<value:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        freq_t = defaultdict(int)
        for char in t:
            freq_t[char]+=1
        bestLen = float("inf")
        bestI = 0
        bestJ = 0
        freq_s = defaultdict(int)
        i = 0
        j = 0
        for i in range(len(s)):
            if (i>0):
                freq_s[s[i-1]]-=1
            while (j<=len(s)):
                
                if (self.check(freq_s,freq_t)):
                    if j-i<bestLen:
                        bestLen = j-i
                        bestI = i
                        bestJ = j
                    break
                if j<len(s):
                    freq_s[s[j]]+=1
                j+=1            

        return s[bestI:bestJ]
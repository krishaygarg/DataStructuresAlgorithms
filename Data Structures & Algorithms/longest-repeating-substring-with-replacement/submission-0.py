class Solution:
    def maxFreq(self, m):
        best = 0
        for key, value in m.items():
            best = max(best, value)
        return best
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        start = 0
        end = 0
        best = 1
        freq[s[0]]+=1
        while (end<len(s)):
            print(start, end, self.maxFreq(freq))
            if (end-start+1<=self.maxFreq(freq)+k):
                best = max(best, end-start+1)
                end+=1
                if end < len(s):
                    freq[s[end]]+=1
            else:
                freq[s[start]]-=1
                start+=1
        return best

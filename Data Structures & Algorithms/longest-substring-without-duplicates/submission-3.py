class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i, j = 0, 0
        best = 0
        while (j<len(s)):
            if (s[j] in seen):
                while i<=j:
                    if s[i]==s[j]:
                        i+=1
                        break
                    else:
                        seen.remove(s[i])
                        i+=1
            else:
                seen.add(s[j])
            best = max(best, j-i+1)
            j+=1
        return best
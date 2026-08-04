class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for word in wordDict:
                if len(word)<=i+1 and s[i-len(word)+1:i+1]==word and dp[i-len(word)+1]:
                    dp[i+1] = True
        return dp[len(s)]


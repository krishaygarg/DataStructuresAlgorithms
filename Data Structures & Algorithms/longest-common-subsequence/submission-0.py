class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        print(dp)
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                a, b, c = 0, 0, 0
                if i>0 and j>0:
                    if text1[i-1]==text2[j-1]:
                        a = 1+dp[i-1][j-1]
                if i>0:
                    b = dp[i-1][j]
                if j>0:
                    c = dp[i][j-1]
                dp[i][j] = max(max(a,b),c)
        return dp[len(text1)][len(text2)]
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')]*(1+len(word2)) for _ in range(1+len(word1))]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if (i==0 and j==0):
                    dp[i][j]=0
                elif (i==0):
                    dp[i][j]=(1+dp[i][j-1])
                elif (j==0):
                    dp[i][j]=(1+dp[i-1][j])
                elif (word1[i-1]==word2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j]=min(min(1+dp[i-1][j-1],1+dp[i][j-1]),1+dp[i-1][j])
        print(dp)
        return dp[len(word1)][len(word2)]
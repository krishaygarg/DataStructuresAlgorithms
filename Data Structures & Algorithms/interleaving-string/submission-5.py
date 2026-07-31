class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1)+len(s2)!=len(s3)):
            return False
        m = len(s1)
        n = len(s2)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m+n+1):
            for pos1 in range(max(i-n,0),min(m+1,i+1)):
                pos2 = i-pos1
                if pos1>0 and s1[pos1-1]==s3[i-1]:
                    dp[pos1][pos2] = dp[pos1][pos2] or dp[pos1-1][pos2]
                if pos2>0 and s2[pos2-1]==s3[i-1]:
                    dp[pos1][pos2] = dp[pos1][pos2] or dp[pos1][pos2-1]
                print(pos1, pos2, dp[pos1][pos2])
        print(dp)
        return dp[m][n]
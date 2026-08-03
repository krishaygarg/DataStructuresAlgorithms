class Solution:
    def numDecodings(self, s: str) -> int:
        ans = [1]
        for i in range(len(s)):
            cur = 0
            if (s[i]!='0'):
                cur+=ans[-1]
            if (i>0 and int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26):
                cur+=ans[-2]
            ans.append(cur)
        print(ans)
        return ans[-1]
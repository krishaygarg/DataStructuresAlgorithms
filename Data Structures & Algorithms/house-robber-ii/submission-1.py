class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums)==1):
            return nums[0]
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        dp2 = [0]*(len(nums)+1)
        dp2[1] = 0
        for i in range(2,len(nums)+1):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i-1])   
        return max(dp[len(nums)-1],dp2[len(nums)])
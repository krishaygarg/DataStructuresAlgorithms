class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -1e9
        total = 0
        for i in range(len(nums)):
            total+=nums[i]
            
            if total < nums[i]:
                total = nums[i]
            best = max(total,best)
        return best
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prevWays = defaultdict(int)
        prevWays[0] = 1
        for i in range(len(nums)):
            curWays = defaultdict(int)
            for key,value in prevWays.items():
                curWays[key-nums[i]]+=value
                curWays[key+nums[i]]+=value
            prevWays = curWays
        return prevWays[target]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        numLeft = 0
        for i in range(len(nums)-1):
            numLeft-=1
            numLeft = max(numLeft,nums[i])
            print(numLeft)
            if numLeft==0:
                return False
        return True
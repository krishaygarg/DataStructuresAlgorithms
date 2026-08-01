class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n+1):
            total^=i
        other = 0
        for i in nums:
            other^=i
        return total^other

        # 000 
        # 001
        # 010
        # 011
        # 100
        # #101
        # 110
        # 111

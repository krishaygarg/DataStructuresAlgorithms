class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        curEnd = 0
        nextEnd = 0
        pos = 0
        while pos < len(nums):
            while pos<=curEnd and pos<len(nums):
                nextEnd = max(nextEnd, pos+nums[pos])
                pos+=1
            curEnd = nextEnd
            count+=1
        return count-1

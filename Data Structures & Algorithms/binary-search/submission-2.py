class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while (start<end):
            middle = (start+end)//2
            if (nums[middle]>target):
                end = middle-1
            elif nums[middle]==target:
                return middle
            else:
                start=middle+1
        if nums[start]==target:
            return start
        return -1
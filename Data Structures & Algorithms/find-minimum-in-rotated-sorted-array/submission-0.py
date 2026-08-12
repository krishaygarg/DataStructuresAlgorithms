class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        # find midpoint
        # compare to last element
        # if midpoint less than last element end = midpoint
        # else begin = midpoint+1
        while (i<j):
            mid = (i+j)//2
            if (nums[mid]<nums[-1]):
                j = mid
            else:
                i = mid+1
        return nums[i]

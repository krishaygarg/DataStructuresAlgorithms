class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find midpoint
        # target = mid -> return target
        # target between mid and end -> begin = mid+1
        # target > end -> end = mid-1
        # target < mid -> end = mid-1

        # mid, target, end
        i = 0
        j = len(nums)-1
        while (i<=j):
            mid = (i+j)//2
            print(i,j,mid)
            if (nums[mid]==target):
                return mid
            if (target<=nums[-1]):
                if (nums[mid]>nums[-1]):
                    i = mid+1
                else:
                    if (target>nums[mid]):
                        i = mid+1
                    else:
                        j = mid-1
            else:
                if (nums[mid]<nums[-1]):
                    j = mid-1
                else:
                    if (target>nums[mid]):
                        i = mid+1
                    else:
                        j = mid-1


        return -1
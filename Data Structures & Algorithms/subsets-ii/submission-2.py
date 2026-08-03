import copy
class Solution:
    def backtrack(self,nums, index):
        if (index == len(nums)):
            self.answer.append(copy.deepcopy(self.current))
            return
        self.current.append(nums[index])
        self.backtrack(nums,index+1)
        self.current.pop()
        while (index != len(nums)-1 and nums[index+1]==nums[index]):
            index+=1

        self.backtrack(nums,index+1)

        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.answer = []
        self.current = []
        self.backtrack(nums, 0)
        return self.answer
import copy
class Solution:
    def backtrack(self,nums, index, included):
        if (index == len(nums)):
            self.answer.append(copy.deepcopy(self.current))
            return
        # if index==0 or (index>0 and (nums[index]!=nums[index-1] or (len(self.current)>0)and self.current[-1]==nums[index])):
        # include if different from prev or prev included
        if (index>0 and nums[index]!=nums[index-1]) or included or index==0:
            self.current.append(nums[index])
            self.backtrack(nums,index+1, True)
            self.current.pop()
        self.backtrack(nums,index+1, False)

        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.answer = []
        self.current = []
        self.backtrack(nums, 0, False)
        return self.answer
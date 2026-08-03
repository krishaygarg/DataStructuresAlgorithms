import copy
class Solution:
    def compute(self, nums, index):
        if (index == len(nums)):
            print(self.current)
            self.answer.append(copy.deepcopy(self.current))
            return
        self.current.append(nums[index])
        self.compute(nums,index+1)
        self.current.pop()
        self.compute(nums,index+1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.current = []
        self.compute(nums,0)
        return self.answer
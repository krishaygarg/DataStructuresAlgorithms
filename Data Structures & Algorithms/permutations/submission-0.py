import copy
class Solution:
    def compute(self,nums):
        if len(self.current)==len(nums):
            self.answer.append(copy.deepcopy(self.current))
            return
        for i in range(len(nums)):
            if (self.visited[i]==False):
                self.visited[i] = True
                self.current.append(nums[i])
                self.compute(nums)
                self.current.pop()
                self.visited[i] = False
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.visited = [False]*len(nums)
        self.current = []
        self.answer = []
        self.compute(nums)
        return self.answer

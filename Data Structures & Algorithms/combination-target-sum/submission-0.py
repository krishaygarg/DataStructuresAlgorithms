import copy
class Solution:
    def backtrack(self,pos, left):
        if left==0:
            self.answer.append(copy.deepcopy(self.current))
        while (pos<len(self.nums) and self.nums[pos]<=left):
            self.current.append(self.nums[pos])
            self.backtrack(pos,left-self.nums[pos])
            self.current.pop()
            pos+=1
            
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.answer = []
        self.current = []
        self.nums = nums
        self.backtrack(0, target)
        return self.answer
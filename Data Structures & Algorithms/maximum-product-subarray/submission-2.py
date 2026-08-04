class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = 1
        best = float('-inf')
        highestNegative = float('-inf')
        for i in range(len(nums)):
            product*=nums[i]
            if product >= 0:
                best = max(best,product)
            else:
                if highestNegative!=float('-inf'):
                    best = max(best,int(product/highestNegative))
                else:
                    best = max(best,product)
                highestNegative = max(highestNegative, product)
            if nums[i]==0:
                product = 1
                highestNegative = float('inf')
        return best

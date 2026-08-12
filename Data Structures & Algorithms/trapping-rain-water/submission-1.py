class Solution:
    # [0,2,0,3,1,0,1,3,2,1]
    #      ^           ^
    def trap(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = len(height)-1
        leftHigh = 0
        rightHigh = 0
        while (left<=right):
            
            if leftHigh<rightHigh:
                leftHigh = max(leftHigh,height[left])
                total+=max(0,min(leftHigh,rightHigh)-height[left])
                left+=1
            else:
                rightHigh = max(rightHigh,height[right])
                total+=max(0,min(leftHigh,rightHigh)-height[right])
                right-=1
        return total
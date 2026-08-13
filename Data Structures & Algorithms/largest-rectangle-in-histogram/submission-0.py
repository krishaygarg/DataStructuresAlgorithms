class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):
            curI = i
            while (len(stack)>0 and stack[-1][0]>heights[i]):
                current = stack.pop()
                best = max(best,current[0]*(i-current[1]))
                curI = current[1]
            stack.append([heights[i],curI])
        return best
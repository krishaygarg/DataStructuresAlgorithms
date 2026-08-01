class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        i = 0
        j = len(heights)-1
        while (i<j):
            best = max(best,(j-i)*min(heights[i],heights[j]))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return best
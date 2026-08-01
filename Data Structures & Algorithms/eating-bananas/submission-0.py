class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = 0
        for p in piles:
            high = max(p, high)
        while (low<high):
            mid = (low+high)//2
            total = 0
            for p in piles:
                total+=p//mid
                if p%mid!=0:
                    total+=1
            if total<=h:
                high = mid
            else:
                low = mid+1
        return high
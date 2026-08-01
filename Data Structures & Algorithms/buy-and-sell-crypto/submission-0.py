class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        lowestSoFar = float("inf")
        for price in prices:
            if price < lowestSoFar:
                lowestSoFar = price
            else:
                best = max(best,price-lowestSoFar)
        return best
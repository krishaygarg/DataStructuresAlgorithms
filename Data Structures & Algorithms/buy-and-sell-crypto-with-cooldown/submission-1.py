class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dpHolding = -prices[0]
        dpNotHolding = [0]
        for i in range(1,len(prices)):
            
            if i>=2:
                dpHolding=max(dpHolding,dpNotHolding[0]-prices[i])
            else:
                dpHolding=max(dpHolding,-prices[i])
            dpNotHolding.append(max(dpNotHolding[-1],prices[i]+dpHolding))
            if (len(dpNotHolding)>2):
                dpNotHolding.pop(0)
        print(dpHolding,dpNotHolding)
        return dpNotHolding[-1]
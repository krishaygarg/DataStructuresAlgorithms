class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dpHolding = [-prices[0]]
        dpNotHolding = [0]
        for i in range(1,len(prices)):
            dpNotHolding.append(max(dpNotHolding[-1],prices[i]+dpHolding[-1]))
            if i>=2:
                dpHolding.append(max(dpHolding[-1],dpNotHolding[-3]-prices[i]))
            else:
                dpHolding.append(max(dpHolding[-1],-prices[i]))
        print(dpHolding,dpNotHolding)
        return dpNotHolding[-1]
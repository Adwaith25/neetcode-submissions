class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_max=0
        profit=0
        for i in range(len(prices)-1,-1,-1):
            p_max=max(p_max,prices[i])
            if(p_max!=prices[i]):
                profit=max(profit,p_max-prices[i])
        return profit



            
        
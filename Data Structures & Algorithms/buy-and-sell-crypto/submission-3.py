class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_p=0
        while(r<len(prices)):
            a=prices[r]-prices[l]
            max_p=max(max_p,a)
            if(a<0):
                l=r
                r+=1
            else:
                r+=1
        return max_p


            
        
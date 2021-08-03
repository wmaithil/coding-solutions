class Solution(object):
    def maxProfit(self, prices):
        
        #if array is empty 
        if(prices is None):
            return 0
        
        maxprofit=0
        profit=0
        minel=prices[0]
        
        for i in prices:
            if(i<=minel):
                minel=i
            else:
                profit=i-minel
                maxprofit=max(profit,maxprofit)
        
        return maxprofit

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        r=0;
        if(prices == []):
            return 0;
        last=prices[0];
        for i in prices:
            if(i-last > 0):
                r+= i-last;
            last=i;
        return r;

s=Solution();
print s.maxProfit([1,2,3,7,4,5,8,9,2,6,3]);
print s.maxProfit([]);

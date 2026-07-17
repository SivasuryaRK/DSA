class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice = []
        minprice = prices[0]
        for i in range(len(prices)):
            if minprice > prices[i]:
                minprice = prices[i]
            maxprice.append(prices[i] - minprice)
        return max(maxprice)
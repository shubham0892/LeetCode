class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        i = 0
        j = 1
        length_prices = len(prices)
        while j < length_prices:
            if prices[i] > prices[j]:
                i += 1
                j +=1
            elif j < length_prices-1 and prices[j] < prices[j+1]:
                j += 1
            else:
                profit += prices[j] - prices[i]
                i = j+1
                j = i+1
        return profit
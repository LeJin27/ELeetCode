
class Solution: 
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for priceIndex in range(1, len(prices)):
            if prices[priceIndex] >= prices[priceIndex - 1]:
                profit += prices[priceIndex] - prices[priceIndex - 1]
        

        return profit

dog = Solution()
prices = [7,1,5,3,6,4]
profit = dog.maxProfit(prices)

print(profit)


"""
Use the greed approach
Tips are to graph out the prices and look at the area where the price goes positive
"""


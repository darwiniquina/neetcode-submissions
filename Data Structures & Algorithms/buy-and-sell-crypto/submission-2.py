class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        # min_index = best day to buy so far
        min_index = 0

        # i = current day we are trying to sell
        for i, value in enumerate(prices):

            # If today's price is cheaper, make it the new buy day
            if prices[i] < prices[min_index]:
                min_index = i

            # Profit if we bought at min_index and sold today
            potential_profit = prices[i] - prices[min_index]

            # Keep the best profit found so far
            if potential_profit > max_profit:
                max_profit = potential_profit

        return max_profit
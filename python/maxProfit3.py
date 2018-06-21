# Buy Stock III
# Description
# Given an array of positive integers representing a stock's price on each day. On each day you can only make one operation: either buy or sell one unit of stock, at any time you can only hold at most one unit of stock, and you can make at most 2 transactions in total. Determine the maximum profit you can make.

# Assumptions

# The give array is not null and is length of at least 2
# Examples

# {2, 3, 2, 1, 4, 5, 2, 11}, the maximum profit you can make is (5 - 1) + (11 - 2) = 13

class Solution(object):
  def maxProfit(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    # DP: divide and run buy stock I
    # Time Complexity: n^2
    profit = 0
    for i in range(0, len(array)):
      profit = max(self.dp(array[0:i]) + self.dp(array[i:len(array)]), profit)
    return profit

  def dp(self, array):
    if not array:
      return 0
    buy, profit = array[0], 0
    for i in range(1, len(array)):
      profit = max(profit, array[i] - buy)
      if array[i] < buy:
        buy = array[i]
    return profit
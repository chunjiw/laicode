# Buy Stock I
# Description
# Given an array of positive integers representing a stock's price on each day. On each day you can only make one operation: either buy or sell one unit of stock and you can make at most 1 transaction. Determine the maximum profit you can make.

# Assumptions

# The given array is not null and is length of at least 2.
# Examples

# {2, 3, 2, 1, 4, 5}, the maximum profit you can make is 5 - 1 = 4

class Solution(object):
  def maxProfit(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    # DP: keep a record of when you buy at the low price
    buy = array[0]
    profit = 0
    for i in range(1, len(array)):
      profit = max(profit, array[i] - buy)
      if array[i] < buy:
        buy = array[i]
    return profit
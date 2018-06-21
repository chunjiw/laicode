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
    # DP: start over when the delta is greater than previous over all profit
    localMax = 0 # keep the stock if no greater delta
    globalMax = 0
    for i in range(1, len(array)):
      delta = array[i] - array[i - 1]
      localMax = max(localMax + delta, delta) 
      globalMax = max(globalMax, localMax)
    return globalMax
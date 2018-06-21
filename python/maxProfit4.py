# Buy Stock IV
# Description
# Given an array of integers representing a stock's price on each day. On each day you can only make one operation: either buy or sell one unit of stock, and at any time you can only hold at most one unit of stock, and you can make at most K transactions in total. Determine the maximum profit you can make.

# Assumptions

# The give array is not null and is length of at least 2
# Examples

# {2, 3, 2, 1, 4, 5, 2, 11}, K = 3, the maximum profit you can make is (3 - 2) + (5 - 1) + (11 - 2)= 14

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54131/Well-explained-Python-DP-with-comments

class Solution(object):
  def maxProfit(self, array, k):
    """
    input: int[] array, int k 
    return: int
    """
    # write your solution here
    # DP: 2D DP as extention of Buy Stock I 
    n = len(array)
    localMax = [0] * n
    globalMax = [[0] * n for _ in range(k + 1)]
    for ki in range(1, k + 1):
      for i in range(1, n):
        delta = array[i] - array[i - 1]
        localMax[i] = max(
          localMax[i - 1] + delta, # extend the current transaction
          globalMax[ki - 1][i - 1] + delta, # one extra transaction
          globalMax[ki - 1][i - 1]) # no extra transaction
        globalMax[ki][i] = max(globalMax[ki][i - 1], localMax[i])
    return globalMax[k][n - 1]
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
    first, second, current = 0, 0, 0
    for i in range(1, len(array)):
      if array[i - 1] <= array[i]:
        current += array[i] - array[i - 1]
      else:  # a transaction finished
        if current > first:
          second = first
          first = current
        elif current > second:
          second = current
        current = 0
    # need to do the same after the final day
    if current > first:
      second = first
      first = current
    elif current > second:
      second = current

    return first + second

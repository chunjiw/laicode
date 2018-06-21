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
    # DP: Run buy stock 1 from left to right, then right to left, and choose the best combination
    # Time Complexity: n
    if not array:
      return 0
    # get left and right
    buy1, profit1, left = array[0], 0, [0]
    sell2, profit2, right = array[-1], 0, [0]   
    for i in range(1, len(array)):
      profit1 = max(profit1, array[i] - buy1)
      left.append(profit1)
      if array[i] < buy1:
        buy1 = array[i]

      profit2 = max(profit2, sell2 - array[-i-1])
      right.append(profit2)
      if array[-i-1] > sell2:
        sell2 = array[-i-1]
    right.reverse()
    # get result
    profit = left[-1]
    for i in range(1, len(array) - 1):
      profit = max(profit, left[i] + right[i + 1])
    return profit
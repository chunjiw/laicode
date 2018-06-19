# Square Root I
# Description
# Given an integer number n, find its integer square root.

# Assumption:

# n is guaranteed to be >= 0.
# Example:

# Input: 18, Return: 4

# Input: 4, Return: 2

class Solution(object):
  def sqrt(self, x):
    """
    input: int x
    return: int
    """
    # write your solution here
    # binary search from 1 to x/2
    if x < 0:
      return -1
    if x < 1:
      return 0
    if x < 4:
      return 1
    left, right = 1, x
    while left < right:
      mid = (left + right) / 2
      if mid * mid < x and x < (mid + 1) * (mid + 1) or mid * mid == x:
        return mid
      if mid * mid < x:
        left = mid + 1
      else:
        right = mid
    return mid


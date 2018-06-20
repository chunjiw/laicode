# Divide Two Integers With Restrictions
# Description
# Given two integers a and b, calculate a / b without using divide/mod operations.

# Examples:

# 0 / 1 = 0

# 1 / 0 = Integer.MAX_VALUE

# -1 / 0 = Integer.MAX_VALUE

# 11 / 2 = 5

# -11 / 2 = -5

# 11 / -2 = -5

# -11 / -2 = -5

 
class Solution(object):
  def divide(self, a, b):
    """
    input: int a, int b
    return: int
    """
    # write your solution here
    # when there are negatives
    if b == 0:
      return 2147483647 
    if a < 0:
      return -self.divide(-a, b)
    if b < 0:
      return -self.divide(a, -b)
    # when there are 0s
    if a == 0:
      if b == 0:
        return "unknown"
      else:
        return 0
    # when b is 1
    if b == 1:
      return a
    # when a < b
    if a < b:
      return 0
    # binary search
    left, right = 1, a
    while left < right:
      mid = (left + right) / 2
      if mid * b <= a < (mid + 1) * b:
        return mid
      if mid * b < a:
        left = mid + 1
      else:
        right = mid
    return left



# Search Insert Position
# Description
# Given a sorted array and a target value, return the index where it would be if it were inserted in order. 

# Assumptions
# If there are multiple elements with value same as target, we should insert the target before the first existing element.

# Examples

# [1,3,5,6], 5 -> 2

# [1,3,5,6], 2 -> 1

# [1,3,5,6], 7 -> 4

# [1,3,3,3,5,6], 3 -> 1

# [1,3,5,6], 0 -> 0


class Solution(object):
  def searchInsert(self, input, target):
    """
    input: int[] input, int target
    return: int
    """
    # write your solution here
    if not input or target <= input[0]:
      return 0
    if target > input[-1]:
      return len(input)
    left, right = 0, len(input) - 1
    while left < right - 1:
      mid = (left + right) / 2
      if input[mid - 1] < target <= input[mid]:
        return mid
      if target <= input[mid]:
        right = mid
      else:
        left = mid
    return right
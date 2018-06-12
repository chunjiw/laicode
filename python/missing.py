# Missing Number II
# Description
# Given an integer array of size N - 1 sorted by ascending order, containing all the numbers from 1 to N except one, find the missing number.

# Assumptions

# The given array is not null, and N >= 1
# Examples

# A = {1, 2, 4}, the missing number is 3
# A = {1, 2, 3}, the missing number is 4
# A = {}, the missing number is 1

class Solution(object):
  def missing(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    if not array:
      return 1
    if len(array) == 1:
      return 3 - array[0]
    # when the missing is at the end
    if array[0] == 2:
      return 1
    if array[-1] == len(array):
      return len(array) + 1
    # binary search
    left, right = 0, len(array) - 1
    while left < right - 1:
      # print "left = " + str(left)
      mid = (left + right) / 2
      if array[left] + 2 == array[left + 1]:
        return left + 2
      if array[mid] == mid + 1:
        left = mid
      elif array[mid] == mid + 2:
        right = mid
      else: # should never happen
        print "error!"
        break
    return left + 2
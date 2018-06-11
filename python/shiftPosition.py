# Shift Position
# Description
# Given an integer array A, A is sorted in ascending order first then shifted by an arbitrary number of positions, For Example, A = {3, 4, 5, 1, 2} (shifted left by 2 positions). Find the index of the smallest number.

# Assumptions

# There are no duplicate elements in the array
# Examples

# A = {3, 4, 5, 1, 2}, return 3
# A = {1, 2, 3, 4, 5}, return 0
# Corner Cases

# What if A is null or A is of zero length? We should return -1 in this case.

class Solution(object):
  def shiftPosition(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    if not array:
      return -1
    if len(array) == 1:
      return 0
    if array[0] < array[-1]:
      return 0
    left, right = 0, len(array) - 1
    while left < right - 1:
      mid = (left + right) / 2
      if array[mid - 1] > array[mid]:
        return mid
      if array[mid] > array[0]:
        left = mid
      else:
        right = mid - 1
    if array[left] < array[right]:
      return left
    return right
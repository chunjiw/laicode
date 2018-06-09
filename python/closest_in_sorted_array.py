# Closest In Sorted Array
# Description
# Given a target integer T and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to T.

# Assumptions

# There can be duplicate elements in the array, and we can return any of the indices with same value.
# Examples

# A = {1, 2, 3}, T = 2, return 1
# A = {1, 4, 6}, T = 3, return 1
# A = {1, 4, 6}, T = 5, return 1 or 2
# A = {1, 3, 3, 4}, T = 2, return 0 or 1 or 2
# Corner Cases

# What if A is null or A is of zero length? We should return -1 in this case.


class Solution(object):
  def closest(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if not array:
      return -1
    left, right = 0, len(array) - 1
    while left < right - 1:
      mid = (left + right) / 2
      if array[mid] == target:
        return mid
      if array[mid] < target:
        left = mid
      else:
        right = mid
    if abs(array[left] - target) < abs(array[right] - target):
      return left
    return right

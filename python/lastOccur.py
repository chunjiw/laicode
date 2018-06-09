# Last Occurrence
# Description
# Given a target integer T and an integer array A sorted in ascending order, find the index of the last occurrence of T in A or return -1 if there is no such index.

# Assumptions

# There can be duplicate elements in the array.

# Examples

# A = {1, 2, 3}, T = 2, return 1
# A = {1, 2, 3}, T = 4, return -1
# A = {1, 2, 2, 2, 3}, T = 2, return 3
# Corner Cases

# What if A is null or A is array of zero length? We should return -1 in this case.


class Solution(object):
  def lastOccur(self, array, target):
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
      if array[mid] <= target:
        left = mid
      else:
        right = mid - 1
    if array[right] == target:
      return right
    if array[left] == target:
      return left
    return -1

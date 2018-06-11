# Total Occurrence
# Description
# Given a target integer T and an integer array A sorted in ascending order, Find the total number of occurrences of T in A.

# Examples

# A = {1, 2, 3, 4, 5}, T = 3, return 1
# A = {1, 2, 2, 2, 3}, T = 2, return 3
# A = {1, 2, 2, 2, 3}, T = 4, return 0
# Corner Cases

# What if A is null? We should return 0 in this case.


class Solution(object):
  def totalOccurrence(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    first = self.firstOcc(array, target)
    if first == -1:
      return 0
    last = self.lastOcc(array, target)
    return last - first + 1


  def firstOcc(self, array, target):
    if not array:
      return -1
    left, right = 0, len(array) - 1
    while left < right - 1:
      mid = (left + right) / 2
      if array[mid] < target:
        left = mid + 1
      else:
        right = mid
    if array[left] == target:
      return left
    if array[right] == target:
      return right
    return -1 
    
  def lastOcc(self, array, target):
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
    
       
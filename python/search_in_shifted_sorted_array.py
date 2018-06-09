# Search In Shifted Sorted Array I
# Description
# Given a target integer T and an integer array A, A is sorted in ascending order first, then shifted by an arbitrary number of positions.

# For Example, A = {3, 4, 5, 1, 2} (shifted left by 2 positions). Find the index i such that A[i] == T or return -1 if there is no such index.

# Assumptions

# There are no duplicate elements in the array.
# Examples

# A = {3, 4, 5, 1, 2}, T = 4, return 1
# A = {1, 2, 3, 4, 5}, T = 4, return 3
# A = {3, 5, 6, 1, 2}, T = 4, return -1
# Corner Cases

# What if A is null or A is of zero length? We should return -1 in this case.


class Solution(object):
  def search(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    # approach: binary search the shifted amount
    if not array:
      return -1
    left, right = 0, len(array) - 1
    # search the shift
    if array[0] > array[-1]:   # if there is a shift
      while left < right - 1:
        mid = (left + right) / 2
        if array[mid] > array[mid + 1]:
          shift = mid
          break
        if array[mid] < array[right]:
          right = mid
        else:
          left = mid
      if left == right - 1:
        shift = left    
      # initial condition for the search of target
      if target <= array[-1]:
        left, right = shift + 1, len(array) - 1
      if target >= array[0]:
        left, right = 0, shift
      
    # binary search for target
    while left <= right:
      mid = (left + right) / 2
      if array[mid] == target:
        return mid
      if array[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1
    
        
      

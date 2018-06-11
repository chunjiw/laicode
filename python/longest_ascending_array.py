# Longest Ascending SubArray
# Description
# Given an unsorted array, find the length of the longest subarray in which the numbers are in ascending order.

# Assumptions

# The given array is not null
# Examples

# {7, 2, 3, 1, 5, 8, 9, 6}, longest ascending subarray is {1, 5, 8, 9}, length is 4.

# {1, 2, 3, 3, 4, 4, 5}, longest ascending subarray is {1, 2, 3}, length is 3.


class Solution(object):
    def longest(self, array):
      """
      array: int[]
      return: int
      """
      # write your solution here
      if not array:
        return 0
      result = 1 
      current = 1
      for i in range(1, len(array)):
        if array[i - 1] < array[i]:
          current += 1
          result = max(result, current)
        else:
          current = 1
      return result
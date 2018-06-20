# Find Local Minimum
# Description
# Given an unsorted integer array, return any of the local minimum's index.

# An element at index i is defined as local minimum when it is smaller than all its possible two neighbors a[i - 1] and a[i + 1]

# (you can think a[-1] = -infinite, and a[a.length] = +infinite)

# Assumptions:

# The given array is not null or empty.
# There are no duplicate elements in the array.

class Solution(object):
  def localMinimum(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    # don't know how to use binary search here
    array.insert(0, -float("inf"))
    array.append(float('inf'))
    for i in range(1, len(array) - 1):
      if array[i] < array[i - 1] and array[i] < array[i + 1]:
        return i - 1
    return 0
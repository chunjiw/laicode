# Given an array of integers, sort the elements in the array in ascending order. The merge sort algorithm should be used to solve this problem.

# Examples

# {1} is sorted to {1}
# {1, 2, 3} is sorted to {1, 2, 3}
# {3, 2, 1} is sorted to {1, 2, 3}
# {4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
# Corner Cases

# What if the given array is null? In this case, we do not need to do anything.
# What if the given array is of length zero? In this case, we do not need to do anything.

class Solution(object):
  def mergeSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if not array or len(array) < 2:
      return array
    return self.merge(self.mergeSort(array[0:len(array)/2]), \
                      self.mergeSort(array[len(array)/2:len(array)]))
  
  def merge(self, arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
      if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
      else:
        result.append(arr2[j])
        j += 1
    while i < len(arr1):
      result.append(arr1[i])
      i += 1
    while j < len(arr2):
      result.append(arr2[j])
      j += 1
    return result
        

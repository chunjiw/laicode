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
    self.msort(array, 0, len(array))
    return array
  
  def msort(self, array, first, last):
    if first >= last - 1:
      return
    mid = (first + last) / 2
    self.msort(array, first, mid)
    self.msort(array, mid, last)
    i, j, k = 0, 0, first
    left = array[first:mid]
    right = array[mid:last]
    while i < len(left) or j < len(right):
      if i >= len(left):
        array[k] = right[j]
        j += 1
      elif j >= len(right):
        array[k] = left[i]
        i += 1
      elif left[i] < right[j]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1
    return
        

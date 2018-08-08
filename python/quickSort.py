class Solution(object):

  def quickSort(self, array):
    self.qsort(array, 0, len(array) - 1)
    return array

  def qsort(self, array, first, last):
    if first >= last:
      return
    i, j = first, last - 1
    pivot = array[last]
    while i <= j:
      if array[i] > pivot:
        array[i], array[j] = array[j], array[i]
        j -= 1
      else:
        i += 1
    array[i], array[last] = array[last], array[i]
    self.qsort(array, first, i - 1)
    self.qsort(array, i + 1, last)

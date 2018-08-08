import quickSort
import mergeSort

if __name__ == "__main__":
  sol = quickSort.Solution()
  array = [4,5,23,6,8,9,5,21,3]
  array = [2,1]
  print sol.quickSort(array)
  print mergeSort.Solution().mergeSort(array)
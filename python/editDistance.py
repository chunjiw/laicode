# Edit Distance
# Description
# Given two strings of alphanumeric characters, determine the minimum number of Replace, Delete, and Insert operations needed to transform one string into the other.

# Assumptions

# Both strings are not null
# Examples

# string one: "sigh", string two : "asith"

# the edit distance between one and two is 2 (one insert "a" at front then replace "g" with "t").

class Solution(object):
  def editDistance(self, one, two):
    """
    input: string one, string two
    return: int
    """
    # write your solution here
    # 2D DP
    m, n = len(one), len(two)
    dmatrix = [[None] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
      dmatrix[i][0] = i
    for j in range(n + 1):
      dmatrix[0][j] = j
    for i in range(m):
      for j in range(n):
        if one[i] == two[j]:
          dmatrix[i + 1][j + 1] = min(dmatrix[i][j], dmatrix[i + 1][j] + 1, dmatrix[i][j + 1] + 1)
        else:
          dmatrix[i + 1][j + 1] = min(dmatrix[i][j] + 1, dmatrix[i + 1][j] + 1, dmatrix[i][j + 1] + 1)
    return dmatrix[m][n]
        
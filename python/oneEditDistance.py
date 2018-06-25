# One Edit Distance
# Description
# Determine if two given Strings are one edit distance.

# One edit distance means you can only insert one character/delete one character/replace one character to another character in one of the two given Strings and they will become identical.

# Assumptions:

# The two given Strings are not null
# Examples:

# s = "abc", t = "ab" are one edit distance since you can remove the trailing 'c' from s so that s and t are identical

# s = "abc", t = "bcd" are not one edit distance


class Solution(object):
  def oneEditDistance(self, s, t):
    """
    input: string s, string t
    return: boolean
    """
    # write your solution here
    m, n = len(s), len(t)
    dmatrix = [[None] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
      dmatrix[i][0] = i
    for j in range(n + 1):
      dmatrix[0][j] = j
    for i in range(m):
      for j in range(n):
        if s[i] == t[j]:
          dmatrix[i + 1][j + 1] = min(dmatrix[i][j + 1] + 1, dmatrix[i + 1][j] + 1, dmatrix[i][j])
        else:
          dmatrix[i + 1][j + 1] = min(dmatrix[i][j + 1] + 1, dmatrix[i + 1][j] + 1, dmatrix[i][j] + 1)
    return dmatrix[m][n] == 1



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
    # O(n) one pass solution
    m, n = len(s), len(t)
    # when same length
    already = False
    if m == n:
      for i in range(m):
        if s[i] != t[i]:
          if not already:
            already = True
          else:
            return False
      return already
    # when different length
    if abs(m - n) > 1:
      return False
    if len(s) - len(t) == 1:
      s, t = t, s
    # s is the shorter one
    i, j = 0, 0
    already = False
    while j < len(t):
      if i == len(s):
        return not already
      if s[i] != t[j]:
        if already:
          return False
        else:
          already = True
          j += 1
      else:
        i += 1
        j += 1
    return already






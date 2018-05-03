# Validate if a given string is numeric.

# Input:  “0”    Output: true

# Input:  “ 0.1 ” Output: true

# Input:  “abc”   Output: false

# Input:  “1 a”   Output: false

# Input:  “2e10”    Output: true


class Solution(object):
  def isNumber(self, s):
    """
    input: string s
    return: boolean
    """
    # specification:
    # 1. is a number
    # .1 is a number
    # e5 is not a number
    # 5e is not a number
    # 1.4e5 is a number
    # 1.4e5.1 is not a number
    # 1.4E5 is a number
    # "  123" is a number
    # "  12 3" is not a number
    # "" is not a number

    # write your solution here
    s = list(s)
    self.removeSpaces(s)
    # linear scan: if invalid character, then return False;
    # if '.' goes after 'e', return False
    flagpoint, flage = False, False
    for ch in s:
      if ch.isdigit():
        continue
      elif ch == '.':
        if flagpoint or flage:
          return False
        else:
          flagpoint = True
        continue
      elif ch == 'e' or ch == 'E':
        if flage:
          return False
        else:
          flage = True
        continue
      else:
        return False
    # 'e' cannot appear at beginning or end
    if s[0].lower() == 'e' or s[-1].lower() == 'e':
      return False
    else:
      return True

  def removeSpaces(self, s):
    while s and s[0] == ' ':
      s.pop(0)
    while s and s[-1] == ' ':
      s.pop()
    return

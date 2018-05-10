# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order.

# Examples

# "()" and "()[]{}", "[{()}()]" are all valid but "(]" and "([)]" are not.

class Solution(object):
  def isValid(self, s):
    """
    input: string s
    return: boolean
    """
    # write your solution here
    if not s:
      return True
    stack = list()
    for ch in s:
      if ch in ['(', '[', '{']:
        stack.append(ch)
      elif ch == ')':
        if not stack or stack[-1] != '(':
          return False
        else:
          stack.pop()
      elif ch == ']':
        if not stack or stack[-1] != '[':
          return False
        else:
          stack.pop()
      elif ch == '}':
        if not stack or stack[-1] != '{':
          return False
        else:
          stack.pop()
      else:
        return False
    return not stack

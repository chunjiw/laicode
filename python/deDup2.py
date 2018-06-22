# Remove Adjacent Repeated Characters II
# Description
# Remove adjacent, repeated characters in a given string, leaving only two characters for each group of such characters. The characters in the string are sorted in ascending order.

# Assumptions

# Try to do it in place.
# Examples

# aaaabbbc is transferred to aabbc
# Corner Cases

# If the given string is null, we do not need to do anything.

class Solution(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if not input:
      return ''
    input = list(input)
    i, j = 1, 1
    repeat = True
    while i < len(input):
      if input[i] == input[i - 1]:
        if not repeat:
          i += 1
        else:
          input[j] = input[i]
          j += 1
          i += 1
          repeat = False
      else:
        repeat = True
        input[j] = input[i]
        j += 1
        i += 1
    return ''.join(input[0:j])


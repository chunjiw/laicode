# Remove Adjacent Repeated Characters III
# Description
# Remove adjacent, repeated characters in a given string, leaving no character for each group of such characters. The characters in the string are sorted in ascending order.

# Assumptions

# Try to do it in place.
# Examples

# aaaabbbc is transferred to c
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
    i, j = 1, 1
    input = list(input)
    while i < len(input):
      if input[i] == input[i - 1]:
        j -= 1
        i += 1
        while i < len(input) and input[i] == input[i - 1]:
          i += 1
      else:
        input[j] = input[i]
        j += 1
        i += 1
    return ''.join(input[0:j])

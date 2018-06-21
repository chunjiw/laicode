# Encode Space
# Description
# In URL encoding, whenever we see an space " ", we need to replace it with "20%". Provide a method that performs this encoding for a given string.

# Examples

# "google/q?flo wer market" -> "google/q?flo20%wer20%market"
# Corner Cases

# If the given string is null, we do not need to do anything.

class Solution(object):
  def encode(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    n = len(input)
    counter = 0
    for c in input:
      if c == ' ':
        counter += 1
    result = [' '] * (n + 2 * counter)
    i = n - 1
    j = len(result) - 1
    while i >= 0:
      if input[i] == ' ':
        result[j] = '%'
        result[j - 1] = '0'
        result[j - 2] = '2'
        j -= 3
      else:
        result[j] = input[i]
        j -= 1
      i -= 1  
    return ''.join(result)
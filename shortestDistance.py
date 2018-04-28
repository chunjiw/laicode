# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class Solution(object):
  def shortestDistance(self, words, word1, word2):
    """
    input: string[] words, string word1, string word2
    return: int
    """
    # write your solution here
    alist = []
    blist = []    
    for i in range(0, len(words)):
      if words[i] is word1:
        alist.append(i)
      if words[i] is word2:
        blist.append(i)
    gmin = len(words)
    for a in alist:
      for b in blist:
        gmin = min(gmin, abs(a - b))
    return gmin
    

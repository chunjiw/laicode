# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

# Write a function to compute all possible states of the string after one valid move.

# For example, given s = "++++", after one move, it may become one of the following states:

# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# If there is no valid move, return an empty list [].

class Solution(object):
  def generatePossibleNextMoves(self, s):
    """
    input: string s
    return: String[]
    """
    # write your solution here
    result = []
    slist = list(s)
    for i in range(0, len(s) - 1):
      if s[i] == '+' and s[i + 1] == '+':
        self.flip(slist, i)
        result.append(''.join(slist))
        self.flip(slist, i)
    return result
  
  def flip(self, slist, i):
    if slist[i] == '+':
      slist[i], slist[i+1] = '-', '-'
    elif slist[i] == '-':
      slist[i], slist[i+1] = '+', '+'
    return slist

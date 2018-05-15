# Given a 2d grid map of 1s (land) and 0s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3

class Solution(object):
  def numIslands(self, grid):
    """
    input: char[][] grid
    return: int
    """
    # write your solution here
    if not grid:
      return 0
    Row = len(grid)
    Col = len(grid[0])
    counted = set()
    result = 0
    for i in range(0, Row * Col):
      if grid[i / Col][i % Col] == '1' and i not in counted:
        self.count(grid, Row, Col, i, counted)
        result += 1
    return result

  def count(self, grid, Row, Col, i, counted):
    if i >= Row * Col or i in counted:
      return
    counted.add(i)
    # if water, count and pass
    if grid[i / Col][i % Col] == '0':
      return
    # if not, count and count neighbor
    if (i % Col) > 0:
      self.count(grid, Row, Col, i - 1, counted)
    if (i % Col) < (Col - 1):
      self.count(grid, Row, Col, i + 1, counted)
    if (i / Col) > 0:
      self.count(grid, Row, Col, i - Col, counted)
    if (i / Col) < (Row - 1):
      self.count(grid, Row, Col, i + Col, counted)
    return





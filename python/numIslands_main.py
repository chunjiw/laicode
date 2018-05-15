import numIslands

if __name__ == "__main__":
  sol = numIslands.Solution()

  grid = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
  sol.count(grid, 4, 5, 18, set())
  print sol.numIslands(grid)

  grid = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
  sol.count(grid, 4, 5, 3, set())
  print sol.numIslands(grid)

  grid = [["1","1","0","0","0"],["0","1","0","0","1"],["1","0","0","1","1"],["0","0","0","0","0"],["1","0","1","0","1"]]
  print sol.numIslands(grid)
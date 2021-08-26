'''
1219. Path with Maximum Gold
Medium

1364

42

Add to List

Share
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

'''


class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.grid = grid
        self.maxgold = 0
        self.visited = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.m, self.n = len(grid), len(grid[0])
        self.temp = 0
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(i, j)
        return self.maxgold

    def dfs(self, x, y):
        if x >= self.m or (x < 0) or (y >= self.n) or (y < 0) or (self.grid[x][y] == 0) or (x, y) in self.visited:
            return
        self.temp += self.grid[x][y]
        if self.temp > self.maxgold:
            self.maxgold = self.temp

        self.visited.append((x, y))
        for i, j in self.directions:
            self.dfs(x + i, y + j)
        self.temp -= self.grid[x][y]
        self.visited.remove((x, y))





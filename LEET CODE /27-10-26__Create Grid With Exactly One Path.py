class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = [['#'] * n for _ in range(m)]

        # Create a unique path along the top row and rightmost column
        for j in range(n):
            grid[0][j] = '.'

        for i in range(m):
            grid[i][n - 1] = '.'

        # Block alternative paths by keeping all other cells as '#'
        return [''.join(row) for row in grid]

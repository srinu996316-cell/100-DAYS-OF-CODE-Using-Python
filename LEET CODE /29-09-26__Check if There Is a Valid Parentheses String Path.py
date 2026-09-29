class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # dp[j] = set of possible balances at cell (i, j)
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                
                # Calculate balance change
                change = 1 if grid[i][j] == '(' else -1

                if i == 0 and j == 0:
                    # Starting cell
                    if change == 1:
                        dp[j].add(1)
                    continue

                possible = set()

                # From the cell above
                if i > 0:
                    possible.update(dp[j])

                # From the cell on the left
                if j > 0:
                    possible.update(dp[j - 1])

                # Calculate new balances
                new_balances = set()

                for balance in possible:
                    new_balance = balance + change

                    # Balance can never be negative
                    if new_balance >= 0:
                        new_balances.add(new_balance)

                dp[j] = new_balances

        # Bottom-right must have balance 0
        return 0 in dp[n - 1]
        

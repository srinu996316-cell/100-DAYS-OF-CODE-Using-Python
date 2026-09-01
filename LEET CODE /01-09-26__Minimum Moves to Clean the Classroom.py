from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        litter = []
        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)
        pos = {p: i for i, p in enumerate(litter)}
        target = (1 << k) - 1

        # best[r][c][mask] = maximum energy reached
        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        
        q = deque([(sr, sc, 0, energy, 0)])
        best[sr][sc][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, e, steps = q.popleft()

            if mask == target:
                return steps

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                nm = mask

                if (nr, nc) in pos:
                    nm |= 1 << pos[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                # Only continue if we reach this state with MORE energy
                if ne > best[nr][nc][nm]:
                    best[nr][nc][nm] = ne
                    q.append((nr, nc, nm, ne, steps + 1))

        return -1

class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        tree = [[0, 0, 0] for _ in range(2 * size)]
        lazy = [0] * (2 * size)

        def apply(node, length, v):
            s, sq, _ = tree[node]
            tree[node][1] = (sq + 2 * v * s + length * v * v) % MOD
            tree[node][0] = (s + length * v) % MOD
            lazy[node] += v

        def push(node, l, r):
            if lazy[node]:
                m = (l + r) // 2
                apply(node * 2, m - l + 1, lazy[node])
                apply(node * 2 + 1, r - m, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, r - l + 1, 1)
                return
            push(node, l, r)
            m = (l + r) // 2
            if ql <= m:
                update(node * 2, l, m, ql, qr)
            if qr > m:
                update(node * 2 + 1, m + 1, r, ql, qr)
            tree[node][0] = (tree[node * 2][0] + tree[node * 2 + 1][0]) % MOD
            tree[node][1] = (tree[node * 2][1] + tree[node * 2 + 1][1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, i)
            last[x] = i
            ans = (ans + tree[1][1]) % MOD

        return ans

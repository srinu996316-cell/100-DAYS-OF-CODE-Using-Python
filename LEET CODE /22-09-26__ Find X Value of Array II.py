class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [None] * (4 * n)

        def merge(a, b):
            p = (a[0] * b[0]) % k
            cnt = a[1][:]
            for i in range(k):
                cnt[a[0] * i % k] += b[1][i]
            return p, cnt

        def build(v, l, r):
            if l == r:
                x = nums[l] % k
                c = [0] * k
                c[x] = 1
                tree[v] = (x, c)
                return
            m = (l + r) // 2
            build(v*2, l, m)
            build(v*2+1, m+1, r)
            tree[v] = merge(tree[v*2], tree[v*2+1])

        def update(v, l, r, p, x):
            if l == r:
                x %= k
                c = [0] * k
                c[x] = 1
                tree[v] = (x, c)
                return
            m = (l + r) // 2
            if p <= m:
                update(v*2, l, m, p, x)
            else:
                update(v*2+1, m+1, r, p, x)
            tree[v] = merge(tree[v*2], tree[v*2+1])

        def query(v, l, r, ql):
            if l >= ql:
                return tree[v]
            m = (l + r) // 2
            if ql > m:
                return query(v*2+1, m+1, r, ql)
            return merge(
                query(v*2, l, m, ql),
                tree[v*2+1]
            )

        build(1, 0, n-1)

        ans = []
        for i, val, start, x in queries:
            update(1, 0, n-1, i, val)
            ans.append(query(1, 0, n-1, start)[1][x])

        return ans

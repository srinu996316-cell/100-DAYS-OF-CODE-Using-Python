class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        L = n.bit_length()
        tin, tout, dep = [0]*n, [0]*n, [0]*n
        par = [[0]*n for _ in range(L)]
        timer = [0]

        def dfs(u, p):
            par[0][u] = p
            tin[u] = timer[0]
            timer[0] += 1
            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    dfs(v, u)
            tout[u] = timer[0]

        dfs(0, 0)
        for j in range(1, L):
            for u in range(n):
                par[j][u] = par[j-1][par[j-1][u]]

        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            d = dep[u] - dep[v]
            for j in range(L):
                if d >> j & 1:
                    u = par[j][u]
            if u == v:
                return u
            for j in range(L-1, -1, -1):
                if par[j][u] != par[j][v]:
                    u, v = par[j][u], par[j][v]
            return par[0][u]

        bit = [0]*(n+1)

        def add(i, x):
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def pref(i):
            x = 0
            while i:
                x ^= bit[i]
                i -= i & -i
            return x

        a = [1 << (ord(c)-97) for c in s]

        def change(u, x):
            add(tin[u]+1, x)
            if tout[u] < n:
                add(tout[u]+1, x)

        for u in range(n):
            change(u, a[u])

        ans = []
        for q in queries:
            z = q.split()
            if z[0] == "update":
                u, x = int(z[1]), 1 << (ord(z[2])-97)
                change(u, a[u] ^ x)
                a[u] = x
            else:
                u, v = int(z[1]), int(z[2])
                x = pref(tin[u]+1) ^ pref(tin[v]+1) ^ a[lca(u, v)]
                ans.append((x & (x-1)) == 0)

        return ans

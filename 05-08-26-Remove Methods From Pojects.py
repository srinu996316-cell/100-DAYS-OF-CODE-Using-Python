class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods using DFS
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if not suspicious[nei]:
                    suspicious[nei] = True
                    stack.append(nei)

        # Check if any outside method calls a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return remaining (non-suspicious) methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans
        

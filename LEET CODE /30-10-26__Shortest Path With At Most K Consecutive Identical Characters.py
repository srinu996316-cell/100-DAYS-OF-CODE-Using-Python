
import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """

        if k <= 0:
            return -1

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        # State: (distance, node, consecutive_count)
        # The last character is labels[node].
        pq = [(0, 0, 1)]

        # dist[node][count] = minimum distance
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        while pq:
            cost, u, cnt = heapq.heappop(pq)

            if cost != dist[u][cnt]:
                continue

            # Reached destination
            if u == n - 1:
                return cost

            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                # Cannot exceed k consecutive characters
                if new_cnt > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_cost
                    heapq.heappush(
                        pq, (new_cost, v, new_cnt)
                    )

        return -1

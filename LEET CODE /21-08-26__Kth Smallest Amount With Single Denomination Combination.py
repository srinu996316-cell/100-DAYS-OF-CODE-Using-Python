class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        coins = sorted(set(coins))
        useful = []

        for c in coins:
            if not any(c % x == 0 for x in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        g = gcd(lcm, coins[i])
                        lcm = (lcm // g) * coins[i]

                        if lcm > x:
                            break

                if lcm > x:
                    continue

                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

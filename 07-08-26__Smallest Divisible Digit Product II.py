class Solution:
    def smallestNumber(self, num, t):

        # Prime factors that can occur in digits 1..9
        primes = [2, 3, 5, 7]

        need = [0, 0, 0, 0]

        # Factorize t
        for i in range(4):
            while t % primes[i] == 0:
                need[i] += 1
                t //= primes[i]

        # If t contains any other prime factor, impossible
        if t != 1:
            return "-1"

        # Factor contribution of each digit
        fac = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        ]

        INF = 10 ** 9

        # ---------------------------------------------------------
        # Minimum number of digits required for a remaining state
        # ---------------------------------------------------------
        memo = {}

        def dp(a, b, c, d):

            key = (a, b, c, d)

            if key in memo:
                return memo[key]

            if a == 0 and b == 0 and c == 0 and d == 0:
                return 0

            best = INF

            for digit in range(2, 10):

                fa, fb, fc, fd = fac[digit]

                na = max(0, a - fa)
                nb = max(0, b - fb)
                nc = max(0, c - fc)
                nd = max(0, d - fd)

                if na == a and nb == b and nc == c and nd == d:
                    continue

                value = dp(na, nb, nc, nd)

                if value + 1 < best:
                    best = value + 1

            memo[key] = best
            return best

        # ---------------------------------------------------------
        # Remove factors supplied by one digit
        # ---------------------------------------------------------
        def reduce_state(state, digit):

            a, b, c, d = state
            fa, fb, fc, fd = fac[digit]

            return (
                max(0, a - fa),
                max(0, b - fb),
                max(0, c - fc),
                max(0, d - fd)
            )

        # ---------------------------------------------------------
        # Construct smallest suffix of given length
        # ---------------------------------------------------------
        def build(length, state):

            result = []

            for pos in range(length):

                remaining = length - pos - 1

                for digit in range(1, 10):

                    ns = reduce_state(state, digit)

                    if dp(*ns) <= remaining:
                        result.append(str(digit))
                        state = ns
                        break

                else:
                    return None

            return ''.join(result)

        n = len(num)

        # ---------------------------------------------------------
        # Count factors in num
        # ---------------------------------------------------------
        total = [0, 0, 0, 0]

        first_zero = n

        for i, ch in enumerate(num):

            digit = ord(ch) - 48

            if digit == 0:

                if first_zero == n:
                    first_zero = i

            else:

                f = fac[digit]

                total[0] += f[0]
                total[1] += f[1]
                total[2] += f[2]
                total[3] += f[3]

        # ---------------------------------------------------------
        # If num itself is valid
        # ---------------------------------------------------------
        if first_zero == n:

            if (
                total[0] >= need[0]
                and total[1] >= need[1]
                and total[2] >= need[2]
                and total[3] >= need[3]
            ):
                return num

        # ---------------------------------------------------------
        # Try to create answer with the SAME length.
        #
        # Scan from right to left.
        # first_zero replaces the previous O(n^2) zero checking.
        # Prefix num[:i] is zero-free iff i <= first_zero.
        # ---------------------------------------------------------

        suffix = [0, 0, 0, 0]

        for i in range(n - 1, -1, -1):

            digit = ord(num[i]) - 48

            # Prefix num[:i] must contain no zero.
            if i <= first_zero:

                f = fac[digit]

                prefix = (
                    total[0] - suffix[0] - f[0],
                    total[1] - suffix[1] - f[1],
                    total[2] - suffix[2] - f[2],
                    total[3] - suffix[3] - f[3]
                )

                # Try the smallest larger digit
                for new_digit in range(digit + 1, 10):

                    nf = fac[new_digit]

                    state = (
                        max(0, need[0] - prefix[0] - nf[0]),
                        max(0, need[1] - prefix[1] - nf[1]),
                        max(0, need[2] - prefix[2] - nf[2]),
                        max(0, need[3] - prefix[3] - nf[3])
                    )

                    remaining = n - i - 1

                    # Can the remaining positions satisfy state?
                    if dp(*state) <= remaining:

                        suffix_answer = build(
                            remaining,
                            state
                        )

                        if suffix_answer is not None:

                            return (
                                num[:i]
                                + str(new_digit)
                                + suffix_answer
                            )

            # Add current digit to suffix factor count
            if digit != 0:

                f = fac[digit]

                suffix[0] += f[0]
                suffix[1] += f[1]
                suffix[2] += f[2]
                suffix[3] += f[3]

        # ---------------------------------------------------------
        # If same length is impossible, use a longer number.
        # ---------------------------------------------------------

        minimum_length = dp(
            need[0],
            need[1],
            need[2],
            need[3]
        )

        if minimum_length == INF:
            return "-1"

        length = max(n + 1, minimum_length)

        answer = build(
            length,
            (
                need[0],
                need[1],
                need[2],
                need[3]
            )
        )

        if answer is None:
            return "-1"

        return answer




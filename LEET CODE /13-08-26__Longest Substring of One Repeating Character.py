class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """

        n = len(s)

        # Each node stores:
        # [left_char, right_char, length, prefix, suffix, best]
        tree = [None] * (4 * n)

        def merge(left, right):
            if left is None:
                return right

            if right is None:
                return left

            left_char, left_right, left_len, left_pre, left_suf, left_best = left
            right_left, right_char, right_len, right_pre, right_suf, right_best = right

            # Total length
            length = left_len + right_len

            # Initially, best is the best from either side
            best = max(left_best, right_best)

            # Initially prefix and suffix remain unchanged
            prefix = left_pre
            suffix = right_suf

            # If the two boundary characters are equal,
            # we can combine suffix of left + prefix of right.
            if left_right == right_left:

                best = max(best, left_suf + right_pre)

                # If the entire left segment has one character,
                # its prefix can extend into the right segment.
                if left_pre == left_len:
                    prefix = left_len + right_pre

                # If the entire right segment has one character,
                # its suffix can extend into the left segment.
                if right_pre == right_len:
                    suffix = right_len + left_suf

            return [
                left_char,
                right_char,
                length,
                prefix,
                suffix,
                best
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = [
                    s[l],   # left_char
                    s[l],   # right_char
                    1,      # length
                    1,      # prefix
                    1,      # suffix
                    1       # best
                ]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build segment tree
        build(1, 0, n - 1)

        result = []

        # Process queries
        for i in range(len(queryCharacters)):
            index = queryIndices[i]
            char = queryCharacters[i]

            update(1, 0, n - 1, index, char)

            # tree[1][5] = longest repeating substring
            result.append(tree[1][5])

        return result

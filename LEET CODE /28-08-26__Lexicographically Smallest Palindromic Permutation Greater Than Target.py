class Solution(object):

    def lexPalindromicPermutation(self, s, target):
        from collections import Counter

        cnt = Counter(s)
        n = len(s)
        m = n // 2

        # Check whether a palindromic permutation is possible
        odd = [c for c in cnt if cnt[c] % 2]
        if len(odd) > 1:
            return ""

        mid = odd[0] if odd else ""

        # Frequency for the left half
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1

        for i in range(26):
            freq[i] //= 2

        prefix = target[:m]
        left = []

        # Try to match target's left half
        i = 0
        while i < m:
            x = ord(prefix[i]) - 97

            if freq[x] > 0:
                left.append(x)
                freq[x] -= 1
                i += 1
            else:
                break

        # If exact prefix cannot be completed,
        # increase the current/previous position
        if i < m:

            # Try increasing at current position
            found = False

            for c in range(ord(prefix[i]) - 96, 26):
                if freq[c] > 0:
                    left.append(c)
                    freq[c] -= 1
                    found = True
                    break

            # Otherwise backtrack
            while not found and left:
                pos = len(left) - 1
                old = left.pop()
                freq[old] += 1

                limit = ord(prefix[pos]) - 97

                for c in range(limit + 1, 26):
                    if freq[c] > 0:
                        left.append(c)
                        freq[c] -= 1
                        found = True
                        break

            if not found:
                return ""

            # Fill remaining positions with smallest characters
            for c in range(26):
                while freq[c] > 0:
                    left.append(c)
                    freq[c] -= 1

        # Build palindrome
        L = ''.join(chr(x + 97) for x in left)
        ans = L + mid + L[::-1]

        # Strictly greater
        if ans > target:
            return ans

        # Left half is equal to target prefix,
        # so find its next lexicographical permutation
        a = left[:]

        i = m - 2
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1

        if i < 0:
            return ""

        j = m - 1
        while a[j] <= a[i]:
            j -= 1

        a[i], a[j] = a[j], a[i]
        a[i + 1:] = reversed(a[i + 1:])

        L = ''.join(chr(x + 97) for x in a)
        return L + mid + L[::-1]

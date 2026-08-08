class Solution(object):
    def validSequence(self, word1, word2):
        import bisect

        n = len(word1)
        m = len(word2)

        # positions[c] = all indices where character c occurs
        # in word1.
        positions = [[] for _ in range(26)]

        for i, ch in enumerate(word1):
            positions[ord(ch) - 97].append(i)

        # exact[j] = latest possible starting index for matching
        # word2[j:] EXACTLY.
        #
        # one[j] = latest possible starting index for matching
        # word2[j:] with AT MOST one mismatch.
        exact = [-1] * (m + 1)
        one = [-1] * (m + 1)

        # Empty suffix can start after the last character.
        exact[m] = n
        one[m] = n

        # run_start / run_end help us find the next character
        # that is different from word1[i].
        run_start = [0] * n
        run_end = [0] * n

        i = 0
        while i < n:
            j = i + 1

            while j < n and word1[j] == word1[i]:
                j += 1

            for k in range(i, j):
                run_start[k] = i
                run_end[k] = j

            i = j

        # ---------------------------------------------------------
        # Build exact[] and one[] from right to left.
        # ---------------------------------------------------------
        for j in range(m - 1, -1, -1):

            arr = positions[ord(word2[j]) - 97]

            # -----------------------------------------------------
            # exact[j]
            #
            # Current character must match exactly and the
            # remaining suffix must also match exactly.
            # -----------------------------------------------------
            limit = exact[j + 1]

            k = bisect.bisect_left(arr, limit) - 1

            if k >= 0:
                exact[j] = arr[k]

            # -----------------------------------------------------
            # one[j]
            #
            # Option 1:
            # Current character matches exactly, and the remaining
            # suffix uses at most one mismatch.
            # -----------------------------------------------------
            limit = one[j + 1]

            k = bisect.bisect_left(arr, limit) - 1

            same = -1

            if k >= 0:
                same = arr[k]

            # -----------------------------------------------------
            # Option 2:
            # Current character is the one mismatch, and the
            # remaining suffix must match exactly.
            # -----------------------------------------------------
            limit = exact[j + 1]

            different = -1

            if limit > 0:
                candidate = limit - 1

                if word1[candidate] != word2[j]:
                    different = candidate
                else:
                    # Skip the whole run of the same character.
                    different = run_start[candidate] - 1

            one[j] = max(same, different)

        # ---------------------------------------------------------
        # Construct lexicographically smallest answer.
        # ---------------------------------------------------------
        ans = []
        prev = -1
        changed = False

        for j in range(m):

            if changed:
                # We already used the one mismatch.
                # Everything from here must match exactly.
                limit = exact[j + 1]

                arr = positions[ord(word2[j]) - 97]

                k = bisect.bisect_right(arr, prev)

                if k >= len(arr):
                    return []

                idx = arr[k]

                if idx >= limit:
                    return []

                ans.append(idx)
                prev = idx

            else:
                # -------------------------------------------------
                # Option 1:
                # Match current character exactly.
                # The suffix may use the one mismatch.
                # -------------------------------------------------
                arr = positions[ord(word2[j]) - 97]

                k = bisect.bisect_right(arr, prev)

                exact_idx = n

                if k < len(arr):
                    candidate = arr[k]

                    if candidate < one[j + 1]:
                        exact_idx = candidate

                # -------------------------------------------------
                # Option 2:
                # Use the mismatch at the current character.
                # Then the suffix must match exactly.
                # -------------------------------------------------
                mismatch_idx = n

                candidate = prev + 1
                limit = exact[j + 1]

                if candidate < limit:

                    if word1[candidate] != word2[j]:
                        mismatch_idx = candidate

                    else:
                        # Skip consecutive equal characters.
                        candidate = run_end[candidate]

                        if candidate < limit:
                            mismatch_idx = candidate

                # No valid choice.
                if exact_idx == n and mismatch_idx == n:
                    return []

                # Choose the smaller index.
                if mismatch_idx < exact_idx:
                    idx = mismatch_idx
                    changed = True
                else:
                    idx = exact_idx

                ans.append(idx)
                prev = idx

        return ans

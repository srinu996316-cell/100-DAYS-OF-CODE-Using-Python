class Solution(object):
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        ans = []
        n = len(s)

        for i in range(n):
            x = ord(target[i]) - 97

            # Try to keep equal
            if cnt[x]:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                # Cannot match, try smallest greater character
                for j in range(x + 1, 26):
                    if cnt[j]:
                        ans.append(chr(j + 97))
                        cnt[j] -= 1
                        return ''.join(ans) + ''.join(
                            chr(k + 97) * cnt[k] for k in range(26)
                        )
                break

        # Backtrack and try increasing a previous position
        while ans:
            i = len(ans) - 1
            c = ans.pop()
            cnt[ord(c) - 97] += 1
            x = ord(target[i]) - 97

            for j in range(x + 1, 26):
                if cnt[j]:
                    ans.append(chr(j + 97))
                    cnt[j] -= 1
                    return ''.join(ans) + ''.join(
                        chr(k + 97) * cnt[k] for k in range(26)
                    )

        return ""

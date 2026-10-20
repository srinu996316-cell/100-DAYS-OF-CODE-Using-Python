class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)
            doubled = a + a
            j = 0
            pi = [0] * k

            for i in range(1, k):
                while j > 0 and b[i] != b[j]:
                    j = pi[j - 1]
                if b[i] == b[j]:
                    j += 1
                pi[i] = j

            j = 0
            for i in range(2 * k - 1):
                while j > 0 and doubled[i] != b[j]:
                    j = pi[j - 1]
                if doubled[i] == b[j]:
                    j += 1
                if j == k:
                    if i - k + 1 < k:
                        return True
                    j = pi[j - 1]

            return False

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for i in range(0, n, k):
                a = nums[i:i + k]
                b = target[i:i + k]

                if not is_rotation(a, b):
                    valid = False
                    break

            if valid:
                ans += k

        return ans

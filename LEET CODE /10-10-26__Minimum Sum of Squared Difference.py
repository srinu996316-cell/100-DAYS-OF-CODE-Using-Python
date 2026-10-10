
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            need = sum(max(0, d - mid) for d in diff)

            if need > k:
                left = mid + 1
            else:
                right = mid

        ans = 0
        remaining = k

        for d in diff:
            reduction = max(0, d - left)
            remaining -= reduction
            ans += (d - reduction) ** 2

        for i in range(len(diff)):
            if remaining > 0 and diff[i] >= left and left > 0:
                ans -= 2 * left - 1
                remaining -= 1

        return ans

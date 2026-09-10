class Solution(object):
    def averageOfSubtree(self, root):
        count = [0]

        def dfs(node):
            if node is None:
                return (0, 0)

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            average = total_sum // total_count

            if node.val == average:
                count[0] += 1

            return (total_sum, total_count)

        dfs(root)
        return count[0]

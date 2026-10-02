
class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open_count, close_count):
            # Base condition
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add opening parenthesis
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add closing parenthesis
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(curr, open_count, close_count):
            # If the current string is a valid combination
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # If we can still add an opening bracket
            if open_count < n:
                backtrack(curr + '(', open_count + 1, close_count)

            # If we can add a closing bracket (only if there is an unmatched opening)
            if close_count < open_count:
                backtrack(curr + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return res

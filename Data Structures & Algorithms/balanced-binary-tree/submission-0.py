class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return (True, 0)

            left_balanced, left_h = dfs(node.left)
            right_balanced, right_h = dfs(node.right)

            balanced = (
                left_balanced and 
                right_balanced and 
                abs(left_h - right_h) <= 1
            )

            return (balanced, 1 + max(left_h, right_h))

        return dfs(root)[0]
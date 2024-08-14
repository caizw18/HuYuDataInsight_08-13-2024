class Solution:
    def flatten(self, root: TreeNode):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        current = root
        while current.right:
            current = current.right

        current.right = right

# Example usage:
# root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
# sol = Solution()
# sol.flatten(root)
# # The tree is now flattened to a linked list.
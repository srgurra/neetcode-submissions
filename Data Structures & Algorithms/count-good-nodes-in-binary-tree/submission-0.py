# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0
        def dfs(node, maxsofar):
            if not node:
                return 0

            nonlocal ans

            if node.val>= maxsofar:
                ans+=1
                maxsofar = node.val
            dfs(node.left, maxsofar)
            dfs(node.right, maxsofar)
            
            return ans

        dfs(root, -math.inf)
        return ans


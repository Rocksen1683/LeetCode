# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverseDepth(root, depth):
            if not root:
                return 0
            return max(traverseDepth(root.left,depth+1),traverseDepth(root.right,depth+1)) + 1
        

        return traverseDepth(root, 0)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res =0 # diameter is stored in res and it is global answer for the entire tree
        #Returns height
        def dfs(root):
            if not root:
             return 0
            
            left = dfs(root.left) # height of left subtree
            right = dfs(root.right)# height of right subtree

            self.res = max(self.res,left + right) #diameter
            return 1 + max(left,right) #height

        dfs(root)
        return self.res


        
        
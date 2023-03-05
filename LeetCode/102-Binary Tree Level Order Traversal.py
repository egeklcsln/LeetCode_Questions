# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    d=[]
    lvl_tmp=[]
    def levelOrder(self, root):
        self.d=[]
        self.lvl_tmp=[]
        self.dfs(root,0)
        return self.d


        
        

    def dfs(self,root,level):
        if root==None:
            return
        if not level in self.lvl_tmp:
            self.d.append([])
            self.lvl_tmp.append(level)


        self.d[level].append(root.val)
        self.dfs(root.left,level+1)
        self.dfs(root.right,level+1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        list=[]
        self.dfs(root,0,list)
        return list
    def dfs(self,node,level,list):
        if not node:
            return
        
        if len(list)<=level:
            list +=[[]]
        self.dfs(node.left,level+1,list)
        self.dfs(node.right,level+1,list)

        if level%2==0:
            list[level].append(node.val)
        else:
            list[level].insert(0,node.val)
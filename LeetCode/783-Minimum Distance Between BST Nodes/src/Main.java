public class Main {

    public static void main(String[] args) {
	// write your code here
    }
}

class Solution {
    TreeNode prev;
    int res;
    public int minDiffInBST(TreeNode root) {
        prev=null;
        res=Integer.MAX_VALUE;
        inOrder(root);
        return res;
    }
    public void inOrder(TreeNode node){
        if (node==null){
            return;
        }

        inOrder(node.left);
        if(prev!=null){
            res=Math.min(res,node.val-prev.val);
        }
        prev=node;
        inOrder(node.right);


    }
}

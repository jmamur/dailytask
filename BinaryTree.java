import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

class TreeNode
{
    int val;
    TreeNode left, right;

    TreeNode(int val)
    {
        this.val = val;
        left = null;
        right = null;
    }
}
public class BinaryTree {
    TreeNode root;

    public int maxDepth(TreeNode root) {
        int height = 0;
        if (root == null)
        {
            return height;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (true)
        {
            int nodeCount = queue.size();
            if (nodeCount == 0)
                return height;
            height ++;
            while (nodeCount > 0)
            {
                TreeNode tmpNode = queue.peek();
                queue.remove();
                if (tmpNode.left != null)
                    queue.add(tmpNode.left);
                if (tmpNode.right != null)
                    queue.add(tmpNode.right);
                nodeCount --;
            }
        }
    }
    public int MaxDeepth(TreeNode root)
    {
        int height = 0;
        if (root == null)
        {
            return height;
        }
        int lHeight = MaxDeepth(root.left);
        int rHeight = MaxDeepth(root.right);
        if (lHeight > rHeight)
            return  lHeight + 1;
        else
            return rHeight + 1;
    }
    public List<TreeNode> searchBST(TreeNode root, int val)
    {
        List<TreeNode> result = new LinkedList<TreeNode>();
        if (root == null)
            return null;
        TreeNode tmpNode = root;
        if(tmpNode.val > val)
            tmpNode = tmpNode.left;
        else if(tmpNode.val < val)
            tmpNode = tmpNode.right;
        else
        {
            result.add(tmpNode);
        }
        return result;
    }

    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null)
            return t2;

        Stack<TreeNode[]> stack = new Stack<>();
        stack.push(new TreeNode[]{t1, t2});
        while (!stack.isEmpty())
        {
            TreeNode[] t = stack.pop();
            if (t[0] == null || t[1] == null)
            {
                continue;
            }
            t[0].val += t[1].val;
            if(t[0].left == null)
                t[0].left = t[1].left;
            else
                stack.push(new TreeNode[]{t[0].left, t[1].left});
            if (t[0].right == null)
                t[0].right = t[1].right;
            else
                stack.push(new TreeNode[]{t[0].right, t[1].right});
        }
        return t1;
    }
    public TreeNode mergeTreesRec(TreeNode t1, TreeNode t2) {
        if (t1 == null)
            return t2;
        if (t2 == null)
            return t1;
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
    }
    public TreeNode invertTree(TreeNode root)
    {
        if (root == null)
            return null;
        TreeNode right = this.invertTree(root.right);
        TreeNode left = this.invertTree(root.left);
        root.left = right;
        root.right = left;
        return root;
    }
    public TreeNode InvertTree(TreeNode root)
    {
        if (root == null) return null;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        while (!queue.isEmpty())
        {
            TreeNode current = queue.poll();
            TreeNode tmp  = current.left;
            current.left = tmp.right;
            current.right = tmp;
            if(current.left != null) queue.add(current.left);
            if(current.right != null) queue.add(current.right);
        }
        return root;
    }
}


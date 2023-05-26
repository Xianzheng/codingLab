import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Queue;
import java.util.List;
public class Tree{

    static class node{

        int value = 0;
        node left, right;

        public node(int value){
            this.value = value;

            left = null;

            right = null;

        }
        
    }

    public void insert(node a,int value){

            
        if (value <= a.value){
            if(a.left != null){
                insert(a.left,value);
            }else{
                a.left= new node(value);

            }
        }else{
            if(a.right != null){
                insert(a.right,value);
            }else{
                a.right= new node(value);

            }

        }
        
    }
    public void printTree(node root){
        if(root != null){
            printTree(root.left);
            System.out.println(root.value);
            printTree(root.right);
           

        }
    }

    public static List<Integer> BFSByQueue(node root) {
        if (root == null) {
            return null;
        }

        Queue<node> queue = new LinkedList<>();
        queue.add(root);

     	//存放遍历结果，然后返回
        List<Integer> result = new ArrayList<>();

        while (!queue.isEmpty()) {
            node treeNode = queue.poll();

            /*
            处理 TreeNode 节点 的逻辑
             */
            result.add(treeNode.value);
            
            
            if (treeNode.left != null) {
                queue.add(treeNode.left);
            }
            if (treeNode.right != null) {
                queue.add(treeNode.right);
            }
        }
        return result;
    }
    public static void main(String[] args) {
        Tree tree = new Tree();
        node r = new node(5);
        tree.insert(r,6);
        tree.insert(r,4);
        tree.insert(r,3);
        tree.insert(r,5);
        tree.printTree(r);
        List<Integer> a = tree.BFSByQueue(r);
        System.out.print(a);

    }
}   
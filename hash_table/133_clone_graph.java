package hash_table;

// https://leetcode.com/problems/clone-graph/solutions/3392175/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/

import java.util.*;

class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

class Solution {
    public Node cloneGraph(Node node) {

        // BFS

        // Special Case
        if (node == null) return null;
        
        Node newNode = new Node(node.val);
        HashMap<Integer, Node> map = new HashMap<>();
        map.put(newNode.val, newNode);

        LinkedList<Node> queue = new LinkedList<>();
        queue.add(node);

        while (!queue.isEmpty()){
            Node n = queue.pop();
            for (Node neighbor : n.neighbors){
                if (!map.containsKey(neighbor.val)){
                    map.put(neighbor.val, new Node(neighbor.val));
                    queue.add(neighbor);
                }
                map.get(n.val).neighbors.add(map.get(neighbor.val));
            }
        }
        return newNode;
    }

    
}
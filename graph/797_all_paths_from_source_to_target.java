package graph;

// https://leetcode.com/problems/all-paths-from-source-to-target/
// https://leetcode.com/problems/all-paths-from-source-to-target/solutions/2969408/simple-java-solution-using-dfs-and-bfs-100-faster/

import java.util.*;

class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
    
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        if (graph.length == 0) return res;
       
        List<Integer> temp = new ArrayList<Integer>();
        temp.add(0);
        
        dfs_helper(graph, 0, res, temp);
        return res;
        
    }

    private void dfs_helper(int[][] graph, int index, List<List<Integer>> res, List<Integer> temp){

        // edge case
        if (index == graph.length - 1){
            res.add(new ArrayList<>(temp));
            return;
        }

        for (int curr : graph[index]){
            temp.add(curr);
            dfs_helper(graph, curr, res, temp);
            temp.remove(temp.size()-1); // backtracking
        }
    }
}
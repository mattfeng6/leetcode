# GRAPH

## dfs & bfs

### dfs - 深度优先搜索
- dfs是可一个方向去搜索，不到黄河不回头。搜不下去了再换方向
```
void dfs(param){
    处理节点
    dfs（selected node）// 递归
    backtracking // 回溯
}
```
```
void backtracking(param){
    if (ending situation){
        store res
        return
    }
    for (selection) {
        deal with node
        backtracking(path, list) // 回溯

    }
}
```

### bfs - 广度优先搜索
- 先把本节点连接的所有节点遍历一遍，走到下个节点的时候再把所有节点遍历一遍


[Reference](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%9B%BE%E8%AE%BA%E6%B7%B1%E6%90%9C%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.md)
package hashtable;

// https://leetcode.com/problems/valid-sudoku/

import java.util.*;

class Solution {
    public boolean isValidSudoku(char[][] board) {

        HashSet<String> set = new HashSet<String>();

        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                char c = board[i][j];
                if (!set.add(c + "row" + i) ||
                    !set.add(c + "col" + j) ||
                    !set.add(c + "sub" + i/3 + " " + j/3))
                    return false;
            }
        }
        return true;
        
    }
}

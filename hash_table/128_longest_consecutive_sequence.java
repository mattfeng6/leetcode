package hash_table;

import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        
        int res = 0;
        HashSet<Integer> set = new HashSet<Integer>();
        
        for (int num : nums) {
            set.add(num);
        }

        for (int i = 0; i < nums.length; i++){
            int count = 1;

            // look left
            int num = nums[i];
            while(set.contains(--num)){
                count++;
                set.remove(num);
            }

            // look right
            num = nums[i];
            while (set.contains(++num)){
                count++;
                set.remove(num);
            }
            res = Math.max(res, count);
        }
        return res;
    }
}
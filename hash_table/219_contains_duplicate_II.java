package hashtable;

// https://leetcode.com/problems/contains-duplicate-ii/solutions/61372/simple-java-solution/

import java.util.*;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        
        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (i > k)
                set.remove(nums[i-k-1]);
            if (!set.add(nums[i]))
                return true;
        }
        return false;
        
    }
}

package twopointers;

// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
    public int removeDuplicates(int[] nums) {
        
        if (nums == null) return 0;
        if (nums.length <= 1) return nums.length;

        int left = 0, right = 1, count = 1;
        while (right < nums.length){
            
            if (nums[right] != nums[right-1]){
                nums[++left] = nums[right];
                count++;
            }
            right++;   
        }
        return count;

    }
}
package two_pointers;

// https://leetcode.com/problems/container-with-most-water/

class Solution {
    public int maxArea(int[] height) {
        
        if (height == null || height.length <= 1)
            return 0;
        
        int currVolumn = 0, maxVolumn = 0;
        int left = 0, right = height.length - 1;
        while (left < right){
            currVolumn = Math.min(height[left], height[right]) * (right - left);
            maxVolumn = Math.max(maxVolumn, currVolumn);
            if (height[left] < height[right]) left++;
            else right--;
        }

        return maxVolumn;
    }
}
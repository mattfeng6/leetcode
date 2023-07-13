# https://www.geeksforgeeks.org/sum-of-all-subarrays/#

from typing import List

# class Solution(object):
def subArraySum(arr: List[int]) -> int:

    res = 0
    n = len(arr)
    for i in range(n):
        res += arr[i] * (n-i) * (i+1)

    return res

arr = [1, 2, 3]
print(subArraySum(arr))

# Chase
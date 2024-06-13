"""
# Problem: Maximum Product Subarray

Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.  A subarray is a contiguous subsequence of the array. This problem requires understanding of dynamic programming and array manipulation. It's a variant of the classic Maximum Subarray problem, but instead of sum, we are looking for product.

Input: An integer array `nums`.
Output: Return the maximum product of the subarray.

**Example:**

Input: nums = [2,3,-2,4]
Output: 6

Explanation: [2,3] has the largest product 6.

"""

from typing import List
from functools import reduce
import operator

# Solution: 1 
# O(n^3) :( I'm learning bruh? :) it works.
def max_product_subarray(numberList: List[int]) -> int:
    n = len(numberList)
    subarrays = [
        numberList[start : end + 1] for start in range(n) for end in range(start, n)
    ]

    # let see maximum product
    return max([reduce(operator.mul, subarray) for subarray in subarrays])


output = max_product_subarray([1, 2, 3])
print(output)

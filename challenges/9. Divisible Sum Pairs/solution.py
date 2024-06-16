"""
Given an array of integers and a positive integer k. Determine the number of (i, j) pairs where i < j and ar[i] + ar[j] is divisible by k.

Example
ar = [1, 2, 3, 4, 5, 6]
k = 5

Three pairs meet the criteria: [1, 4], [2, 3], [4, 6]

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

- n: the integer length of array ar
- ar: an array of integers
- k: the integer to divide the pair sum by

Input Format
The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers describing the values of ar.

return
- int: the number of pairs
"""

from typing import List

# O(n^2), I know it's worse but Just learning dude :(
def divisible_sum_pairs(n: int, arr: List[int], k: int):
    # Well, let's also store the paris too (it is out of question)
    pairs = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            pairs.append([arr[i], arr[j]]) if (arr[i] + arr[j]) % k == 0 else ""

    return len(pairs)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    k = 5

    output = divisible_sum_pairs(n, arr, k)
    print(output)

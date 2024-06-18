"""
Given an array of integers, where all elements but one occur twice, find the unique element.

Example:
a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4.

Function Description
Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):
- int a[n]: an array of integers

Returns
- int: the element that occurs only once

Input Format
The first line contains a single integer, n, the number of integers in the array.
The second line contains n space-separated integers that describe the elements in a.

Constraints
- 1 <= n < 100
- It is guaranteed that n is an odd number and that there is one unique element.
- 0 <= a[i] <= 100, where 0 <= i < n.
"""

from typing import List


def lonelyinteger(integers: List[int]):
    i = 0

    for number in integers:
        i ^= number

    return i


if __name__ == "__main__":
    output = lonelyinteger([1, 2, 3, 4, 3, 2, 1])
    print(output)

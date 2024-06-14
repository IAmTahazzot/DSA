"""
# Min-Max sum

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

example:

arr = [1, 3, 5, 7, 9]
The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. The function prints 16 24

## Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):
  arr: an array of 5 integers

## Print:
print the minimum sum and the maximum sum as two space-separated integers on one line.
"""

from typing import List


def min_max_sum(arr: List[int]) -> None:
    arr.sort()

    min_sum = sum(arr[0:4])
    max_sum = sum(arr[-4:])

    print(f"{min_sum} {max_sum}")


if __name__ == "__main__":
    min_max_sum([1, 3, 5, 7, 9])

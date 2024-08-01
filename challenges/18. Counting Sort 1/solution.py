"""
# Counting Sort 1

Comparison sorting:

Quicksort usually has a running time of n * log(n), but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat n * log(n) (worst-case) running time, since n * log(n) represents the minimum number of comparisons needed to know where to place each element.

Alternative Sorting:

Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

Example:

arr = [1, 1, 3, 2, 1] # for this demo input value won't be greater than 100

Return the sorted array: [1, 1, 1, 2, 3]

Sample Input:

```python
arr = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 38, 30, 44, 88, 60, 64, 74, 92, 41, 48, 56, 6, 13, 37, 56, 1, 32, 37, 32, 78, 24, 35, 61, 18, 98, 74, 56, 18, 57, 55, 79, 37, 78, 60, 39, 53, 34, 7, 41, 2, 64, 83, 5, 58, 37, 28, 75, 52, 25, 95, 26, 19, 71, 48, 84, 50, 2, 25, 95, 59, 11, 30, 44, 100, 81, 58, 41, 51, 64, 88, 5, 44, 47, 95, 87, 87, 85, 33, 57, 87, 86, 42, 69, 74, 40, 16, 2, 61, 79, 99, 34, 6, 30, 44, 99, 76, 84, 83, 53, 34, 48, 29, 50, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]
```

Sample Output:

```python
[0, 2, 0, 2, 0, 0, 1, 0, 1, 2, 1, 0, 1, 1, 0, 0, 2, 0, 1, 0, 1, 2, 1, 1, 1, 3, 0, 2, 0, 0, 2, 0, 3, 3, 1, 0, 0, 0, 0, 2, 2, 1, 1, 1, 2, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 2, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 3, 2, 0, 0, 2, 1, 2, 1, 0, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 0, 3, 2, 1, 1, 0, 1, 1, 1, 0, 2, 2]
```
"""


def counting_sort(list):
    new_arr = [0 for _ in range(0, 101)]

    for n in list:
        new_arr[n] += 1

    return new_arr


if __name__ == "__main__":
    output = counting_sort([1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 99, 100])
    print(output)

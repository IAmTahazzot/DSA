"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15 - 17| = 2.
"""


def diagonals_diff(matrix) -> int:
    left_right = []
    right_left = []

    for i in range(len(matrix)):
        left_right.append(matrix[i][i])
        right_left.append(matrix[i][len(matrix) - 1 - i])

    return abs(sum(left_right) - sum(right_left))


if __name__ == "__main__":
    output = diagonals_diff([[1, 2, 3], [4, 5, 6], [9, 8, 9]])
    print(output)

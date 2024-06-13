"""
# Numbe of rectangles that can form the largest square

input: rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
output: 3

[5, 3, 5, 5]

largest is 5 and 3 times (ans)
"""

from typing import List


def countReactanglesOfLargestSquares(rectangleData: List[List[int]]):
    squares = []

    # get all the squares
    for i in range(len(rectangleData)):
        length, width = rectangleData[i]
        squares.append(length if length == width else min(length, width))

    # number of rectangle with largest square
    return squares.count(max(squares))


if __name__ == "__main__":
    rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
    output = countReactanglesOfLargestSquares(rectangles)

    print(output)

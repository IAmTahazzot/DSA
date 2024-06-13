from typing import List


# Solution: 2
# O(n) :) After a little bit more brainstorm
def max_product_subarray2(nums: List[int]) -> int:
    # Initialize maximum and minimum product for the first number
    max_product = nums[0]
    min_product = nums[0]
    result = max_product

    # Iterate over the rest of the numbers
    for num in nums[1:]:
        # If the number is negative, swap the maximum and minimum product
        if num < 0:
            max_product, min_product = min_product, max_product

        # Update the maximum and minimum product
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        # Update the result
        result = max(result, max_product)

    return result


output = max_product_subarray2([2, 3, -2, 4])
print(output)  # Output: 6

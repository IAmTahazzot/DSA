/*
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

arr = [1, 1, 0, -1, -1]

it will be printed as:
0.400000
0.400000
0.200000
*/

#include <stdio.h>
#include <stdbool.h>

void Solution(int length, int *arr)
{
    double positive = 0;
    double negative = 0;
    double zero = 0;

    for (int i = 0; i < length; i++)
    {
        const int value = arr[i];

        if (value == 0)
        {
            zero += 1;
        }
        else if (value < 0)
        {
            negative += 1;
        }
        else if (value > 0)
        {
            positive += 1;
        }
    }

    // getting ratio
    printf("%.6f\n", positive / length);
    printf("%.6f\n", negative / length);
    printf("%.6f\n", zero / length);
}

int main(void)
{
    int arr[] = {1, 1, 0, -1, -1};
    int length = sizeof(arr) / sizeof(arr[0]);

    Solution(length, arr);
    return 0;
}
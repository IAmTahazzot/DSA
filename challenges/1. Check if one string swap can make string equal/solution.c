/**
 *
 * Problem: Given two string with equal length, check if it's possible to make them equal by swapping at most one character.
 *
 * Example:
 * 1. Input: s1 = "bank", s2 = "kanb"
 *   Output: true
 * 2. Input: s1 = "Katheryn" s2 = "Kahteryn"
 *   Output: true
 * 3. Input: s1 = "Winnick" s2 = "Kathery"
 *   Output: false
 */
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isPermutationPossibleWithSwap(char *s1, char *s2)
{
    int diff = 0;
    int diffIndex[2];
    for (int i = 0; i < strlen(s1); i++)
    {
        if (s1[i] != s2[i])
        {
            diff++;
            if (diff > 2)
            {
                return false;
            }
            diffIndex[diff - 1] = i;
        }
    }
    if (diff == 0)
    {
        return true;
    }
    if (diff == 2)
    {
        return s1[diffIndex[0]] == s2[diffIndex[1]] && s1[diffIndex[1]] == s2[diffIndex[0]];
    }
    return false;
}

int main()
{
    char s1[] = "bank";
    char s2[] = "kanb";
    printf("%d\n", isPermutationPossibleWithSwap(s1, s2));

    char s3[] = "Katheryn";
    char s4[] = "Kahteryn";
    printf("%d\n", isPermutationPossibleWithSwap(s3, s4));

    char s5[] = "Winnick";
    char s6[] = "Kathery";
    printf("%d\n", isPermutationPossibleWithSwap(s5, s6));

    return 0;
}
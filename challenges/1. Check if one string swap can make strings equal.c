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

bool solution(char *str1, char *str2);

int main(void)
{
  char str1[] = "somewhere";
  char str2[] = "soeewherm";
  if (solution(str1, str2))
  {
    printf("true\n");
  }
  else
  {
    printf("false\n");
  }
  return 0;
}

bool solution(char *str1, char *str2)
{
  int len = strlen(str1);
  int diff = 0;
  for (int i = 0; i < len; i++)
  {
    if (str1[i] != str2[i])
    {
      diff++;
    }
  }
  if (diff == 2)
  {
    return true;
  }
  return false;
}
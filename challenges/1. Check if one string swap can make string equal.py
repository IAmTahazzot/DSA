"""
Problem: Given two strings with equal length, check if it's possible to make them equal by swapping at most one character.

Example:
1. Input: s1 = "bank", s2 = "kanb"
  Output: true
2. Input: s1 = "Katheryn" s2 = "Kahteryn"
  Output: true
3. Input: s1 = "Winnick" s2 = "Kathery"
  Output: false
"""


def solution(str1: str, str2: str) -> bool:
    invalidIndex = []
    LENGTH = len(str1)

    for i in range(LENGTH):  # both string length is equal
        if str1[i] != str2[i]:
            invalidIndex.append(i)

    if len(invalidIndex) < 2:
        return False

    str2_after_swaped = ""

    for i in range(LENGTH):
        if i == invalidIndex[0]:
            str2_after_swaped += str2[invalidIndex[1]]
        elif i == invalidIndex[1]:
            str2_after_swaped += str2[invalidIndex[0]]
        else:
            str2_after_swaped += str2[i]

    return len(invalidIndex) == 2 and str1 == str2_after_swaped


if __name__ == "__main__":
    print(solution("bank", "kanb"))
    print(solution("Katheryn", "Kahteryn"))
    print(solution("Winnick", "Kathery"))
    print(solution("abcd", "acbd"))

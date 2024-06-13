import unittest

def solution(str1: str, str2: str) -> bool:
    invalidIndex = []
    LENGTH = len(str1)

    for i in range(LENGTH):  # both string length is equal
        if str1[i] != str2[i]:
            invalidIndex.append(i)

    if len(invalidIndex) == 0:
        return True

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


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertTrue(solution("bank", "kanb"))
        self.assertTrue(solution("Katheryn", "Kahteryn"))
        self.assertFalse(solution("Winnick", "Kathery"))
        self.assertFalse(solution("abc", "adc"))
        self.assertTrue(solution("abcd", "abdc"))
        self.assertTrue(solution("abcd", "acbd"))
        self.assertTrue(solution("a", "a"))  # identical single-character strings
        self.assertFalse(solution("a", "b"))  # different single-character strings
        self.assertTrue(solution("", ""))  # empty strings
        self.assertTrue(solution("aa", "aa"))
        self.assertFalse(solution("aa", "ab"))
        self.assertTrue(solution("abc", "acb"))
        self.assertFalse(solution("abcd", "abce"))
        self.assertFalse(solution("abcd", "badc"))
        self.assertFalse(solution("abcd", "dcba"))

if __name__ == "__main__":
    unittest.main()

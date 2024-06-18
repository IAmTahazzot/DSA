"""
HackerLand University has the following grading policy:

- Every student receives a grade in the inclusive range from 0 to 100.
- Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:

- If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
- If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Examples:
- grade = 84 round to 85 (85 - 84 is less than 3)
- grade = 29 do not round (result is less than 40)
- grade = 57 do not round (60 - 57 is 3 or higher)

Return:
- int: the rounded grade
"""

from typing import List


def grading_student(grades: List[int]):
    # Using list comprehension
    # return [grade + (5 - grade % 5) if grade % 5 > 2 and grade > 37 else grade for grade in grades]

    # Using map function
    return list(map(lambda grade: grade + (5 - grade % 5) if grade % 5 > 2 and grade > 37 else grade, grades))


# Sample Test
if __name__ == "__main__":
    output = grading_student([84, 29, 57])
    print(output)

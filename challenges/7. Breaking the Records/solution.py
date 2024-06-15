"""
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

Example:

scroes = [12, 24, 10, 24]
Scores are in the same order as the games played. She tabulates her results as follows:

Game  Score  Minimum  Maximum   Min Max
0      12     12       12       0   0
1      24     12       24       0   1
2      10     10       24       1   1
3      24     10       24       1   1


Returns

int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
"""

from typing import List


def breakingRecords(scores: List[int]):
    currentLeastPoint = currentMostPoint = scores[0]
    leastPoints = mostPoints = 0

    for i in range(len(scores)):
        if currentMostPoint < scores[i]:
            # new breaking point
            mostPoints += 1
            currentMostPoint = scores[i]
        elif currentLeastPoint > scores[i]:
            # new least point
            leastPoints += 1
            currentLeastPoint = scores[i]

    return [mostPoints, leastPoints]


if __name__ == "__main__":
    print(breakingRecords([12, 24, 10, 24]))

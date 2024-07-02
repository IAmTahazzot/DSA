"""
# Counting valleys

## Problem

An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly `steps` steps, for every step it was noted if it was an uphill, `U`, or a downhill, `D` step. Hikes always start and end at sea level, and each step up or down represents a `1` unit change in altitude. We define the following terms:

- A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
- A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

## Function Description

Complete the countingValleys function in the editor below. countingValleys has the following parameter(s):

- int steps: the number of steps on the hike
- string path: a string describing the path

Returns

- int: the number of valleys traversed

Example

```
path = 'UDDDUDUU'
steps = 8
```

The hiker first enters a valley `2` units deep. Then they climb out and up onto a mountain `2` units high. Finally, the hiker returns to sea level and ends the hike.

"""

def counting_valleys(steps, path):
    # Let's say 0 is the sea level below 0 means valleys and above is mountains
    valleys_traversed = current_step = 0

    for step_index in range(steps):
        step_letter = path[step_index]

        # 0 - 1 (entering a valley), add it
        if current_step == 0 and step_letter == "D":
            valleys_traversed += 1

        # updating current_step
        current_step += 1 if step_letter == "U" else -1

    return valleys_traversed


print(counting_valleys(8, "UDDDUDUU"))

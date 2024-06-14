"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

# 07:05:45PM
# 19:05:45


def solution(time: str) -> str:
    IS_AM = time[-2:].lower() == "am"
    hours, minutes, seconds = time[0:-2].split(":")

    new_hour = (
        "00"
        if hours == "12" and IS_AM
        else str(12 + int(hours)) if not IS_AM and not hours == "12" else hours
    )

    return ":".join([new_hour, minutes, seconds])


if __name__ == "__main__":
    print(solution("07:05:45PM"))
    print(solution("12:00:00PM"))

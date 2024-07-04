"""
# Figure out how many "SOS" were altered during the transmission of the message from Mars to Earth and return the count.
"""


def marsExploration(s):
    n = 0

    for i in range(0, len(s), 3):
        n += sum([s[i] != "S", s[i + 1] != "O", s[i + 2] != "S"])

    return n


# print(marsExploration("SOSSPSSQSSOR") == 3)
# print(marsExploration("SOSSOT") == 1)
# print(marsExploration("SOSSOS") == 0)

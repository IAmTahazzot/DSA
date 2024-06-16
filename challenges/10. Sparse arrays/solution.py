"""
There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

Example:

strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']

There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, results = [2, 1, 0].

Function Description

Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

strings strings[n] - an array of strings to search
queries queries[q] - an array of query strings

Returns

- int[q]: an array of results for each query
"""

from typing import List


def matchingStrings(word_list: List[str], queries: List[str]):
    words_counter = {}

    for word in word_list:
        words_counter[word] = words_counter.get(word, 0) + 1

    return [words_counter.get(query, 0) for query in queries]


if __name__ == "__main__":
    strings = ["ab", "ab", "abc"]
    queries = ["ab", "abc", "bc"]
    output = matchingStrings(strings, queries)

    print(output)

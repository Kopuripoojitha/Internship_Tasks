
# Problem: Company Logo
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

if __name__ == '__main__':
    s = input()

    counts = Counter(s)
    result = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for character, count in result[:3]:
        print(character, count)

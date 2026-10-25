# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))

size_count = Counter(shoe_sizes)

N = int(input())
earnings = 0

for i in range(N):
    size, price = map(int, input().split())

    if size_count[size] > 0:
        earnings += price
        size_count[size] -= 1

print(earnings)

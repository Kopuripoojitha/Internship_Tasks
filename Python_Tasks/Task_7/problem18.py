
# Problem: String Construction
# HackerRank: https://www.hackerrank.com/challenges/string-construction/problem

p = int(input())

for _ in range(p):
    s = input().strip()
    print(len(set(s)))

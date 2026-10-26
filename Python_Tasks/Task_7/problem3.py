
# Problem: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()

expected = "SOS" * (len(s) // 3)

changes = 0

for i in range(len(s)):
    if s[i] != expected[i]:
        changes += 1

print(changes)

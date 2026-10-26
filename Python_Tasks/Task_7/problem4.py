
# Problem: Funny String
# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem

t = int(input())

for _ in range(t):
    s = input().strip()
    rev = s[::-1]

    funny = True

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(rev[i]) - ord(rev[i - 1])):
            funny = False
            break

    if funny:
        print("Funny")
    else:
        print("Not Funny")

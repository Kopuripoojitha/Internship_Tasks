
# Problem: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

q = int(input())

for _ in range(q):
    s = input().strip()
    found = False

    for i in range(1, len(s) // 2 + 1):
        first = s[:i]

        if first[0] == "0":
            continue

        num = int(first)
        expected = first

        while len(expected) < len(s):
            num += 1
            expected += str(num)

        if expected == s:
            print("YES", first)
            found = True
            break

    if not found:
        print("NO")


# Problem: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem

s = input().lower()

letters = set()

for char in s:
    if char.isalpha():
        letters.add(char)

if len(letters) == 26:
    print("pangram")
else:
    print("not pangram")

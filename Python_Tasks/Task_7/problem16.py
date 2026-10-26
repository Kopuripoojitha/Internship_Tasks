
# Problem: Caesar Cipher
# HackerRank: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

n = int(input())
s = input().strip()
k = int(input())

k = k % 26
result = ""

for char in s:
    if char.islower():
        new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        result += new_char
    elif char.isupper():
        new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        result += new_char
    else:
        result += char

print(result)


# Problem: Set .intersection() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

common_students = english.intersection(french)

print(len(common_students))

# Problem: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique_numbers = set(array)
    result = sum(unique_numbers) / len(unique_numbers)
    return round(result, 3)

n = int(input())
arr = list(map(int, input().split()))

print(average(arr))

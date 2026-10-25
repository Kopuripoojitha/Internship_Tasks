# Problem: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique_numbers = set(array)
    return round(sum(unique_numbers) / len(unique_numbers), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    result = average(arr)
    print(result)

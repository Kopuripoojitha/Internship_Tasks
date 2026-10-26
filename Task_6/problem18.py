
# Problem: Set Mutations
# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
set_a = set(map(int, input().split()))

operations = int(input())

for _ in range(operations):
    command, length = input().split()
    other_set = set(map(int, input().split()))

    if command == "update":
        set_a.update(other_set)
    elif command == "intersection_update":
        set_a.intersection_update(other_set)
    elif command == "difference_update":
        set_a.difference_update(other_set)
    elif command == "symmetric_difference_update":
        set_a.symmetric_difference_update(other_set)

print(sum(set_a))

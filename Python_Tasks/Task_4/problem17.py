# Problem: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for i in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_marks[name] = marks

    query_name = input()

    total = sum(student_marks[query_name])
    average = total / len(student_marks[query_name])

    print("{:.2f}".format(average))

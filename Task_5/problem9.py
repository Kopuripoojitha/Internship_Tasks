# Problem: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    word_count = OrderedDict()

    for i in range(n):
        word = input()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(len(word_count))
    print(*word_count.values())

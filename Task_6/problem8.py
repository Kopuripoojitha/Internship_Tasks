
# Problem: Tuples
# HackerRank: https://www.hackerrank.com/challenges/python-tuples/problem

def old_tuple_hash(values):
    mask = (1 << 64) - 1

    def signed(value):
        value = value & mask
        if value >= (1 << 63):
            value -= (1 << 64)
        return value

    x = 0x345678
    multiplier = 1000003

    for i, value in enumerate(values):
        remaining = len(values) - i - 1
        x = signed((x ^ value) * multiplier)
        multiplier = signed(multiplier + 82520 + 2 * remaining)

    x = signed(x + 97531)

    if x == -1:
        x = -2

    return x


if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(old_tuple_hash(integer_list))

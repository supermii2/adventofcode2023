import math

from src.solution import Solution
from src.utils import split_by_nextline


def calculate(line):
    length = len(line)
    s = 0
    for i, n in enumerate(reversed(line)):
        s += n * math.comb(length, i + 1) * ((-1) ** i)
    return s


def calculate_bonus(line):
    length = len(line)
    s = 0
    for i, n in enumerate(line):
        s += n * math.comb(length, i + 1) * ((-1) ** i)
    return s


def day9_main(input_string):
    lines = [[int(num) for num in x.split(" ")] for x in split_by_nextline(input_string)]
    return sum([calculate(line) for line in lines])


def day9_bonus(input_string):
    lines = [[int(num) for num in x.split(" ")] for x in split_by_nextline(input_string)]
    return sum([calculate_bonus(line) for line in lines])


if __name__ == "__main__":
    Solution(day9_main).solve()
    Solution(day9_bonus).solve()

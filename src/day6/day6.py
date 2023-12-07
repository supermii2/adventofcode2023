from src.solution import Solution
from src.utils import split_by_nextline

import re
import math


def mod_floor(x):
    if x != math.floor(x):
        return math.floor(x)
    else:
        return int(x - 1)


def mod_ceil(x):
    if x != math.ceil(x):
        return math.ceil(x)
    else:
        return int(x + 1)


def get_number_of_times(time, distance):
    lower_bound = mod_ceil(0.5 * (time - (time ** 2 - (4 * distance)) ** 0.5))
    upper_bound = mod_floor(0.5 * (time + (time ** 2 - (4 * distance)) ** 0.5))
    return upper_bound - lower_bound + 1


def day6_main(input_string):
    times, distances = [[int(x) for x in re.sub(' +', ' ', line.split(":")[1]).split(" ")[1:]] for line in
                        split_by_nextline(input_string)]
    nums = [get_number_of_times(t, d) for t, d in zip(times, distances)]
    return math.prod(nums)


def day6_bonus(input_string):
    times, distances = [[int(line.split(":")[1].replace(" ", ""))] for line in
                        split_by_nextline(input_string)]

    nums = [get_number_of_times(t, d) for t, d in zip(times, distances)]
    return math.prod(nums)


if __name__ == "__main__":
    Solution(day6_main).solve()
    Solution(day6_bonus).solve()

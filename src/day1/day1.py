import re
from src.solution import Solution
from src.utils import split_by_nextline


def day1_main(input_string):
    calibration_strings = split_by_nextline(input_string)
    filtered_calibration_strings = [re.sub("[^0-9]", "", s) for s in calibration_strings]

    return sum([int(s[0] + s[-1]) for s in filtered_calibration_strings])


def day1_bonus(input_string):
    digit_names = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    def get_first_num(s: str):
        for i in range(len(s)):
            if s[i].isnumeric():
                return s[i]

            for digit_name in digit_names:
                if s[i:].startswith(digit_name):
                    return digit_names[digit_name]

    def get_last_num(s: str):
        for i in reversed(range(len(s))):
            if s[i].isnumeric():
                return s[i]

            for digit_name in digit_names:
                if s[:i+1].endswith(digit_name):
                    return digit_names[digit_name]

    calibration_strings = split_by_nextline(input_string)
    filtered_calibration_strings = [int(get_first_num(s) + get_last_num(s)) for s in calibration_strings]
    return sum(filtered_calibration_strings)


if __name__ == "__main__":
    # Solution(day1_main).solve()
    Solution(day1_bonus).solve()

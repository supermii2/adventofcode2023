def split_by_nextline(input_string):
    return input_string.split("\n")


def split_by_empty_line(input_string):
    return input_string.split("\n\n")


def split_n_lines(input_string, n):
    lines = split_by_nextline(input_string)
    return [lines[i:i + n] for i in range(0, len(lines), n)]


def map_int(lst):
    return [int(item) for item in lst]

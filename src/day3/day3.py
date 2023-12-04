from src.solution import Solution
from src.utils import split_by_nextline

adjacency_vectors = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


def day3_main(input_string):
    schematic = split_by_nextline(input_string)

    def adjacent_to_symbol(s, x, y):
        for direction in adjacency_vectors:
            if 0 <= x + direction[0] < len(s) and 0 <= y + direction[1] < len(s[0]):
                ch = s[x + direction[0]][y + direction[1]]
                if not ch.isnumeric() and ch != ".":
                    return True

        return False

    validity_flag = False
    result = 0
    total = 0

    for i, row in enumerate(schematic):
        for j, symbol in enumerate(row):
            if symbol.isnumeric():
                total = total * 10 + int(symbol)
                validity_flag = validity_flag or adjacent_to_symbol(schematic, i, j)
                if not (j + 1 < len(row) and row[j + 1].isnumeric()):
                    result += total if validity_flag else 0
                    total = 0
                    validity_flag = False
            else:
                total = 0
                validity_flag = False

    return result


def day3_bonus(input_string):
    def adjacent_to_gear(s, x, y):
        gear_locations = set()
        for direction in adjacency_vectors:
            if 0 <= x + direction[0] < len(s) and 0 <= y + direction[1] < len(s[0]):
                ch = s[x + direction[0]][y + direction[1]]
                if ch == "*":
                    gear_locations.add((x + direction[0], y + direction[1]))
        return gear_locations

    schematic = split_by_nextline(input_string)
    gears = {}
    gear_coordinates = set()
    total = 0

    for i, row in enumerate(schematic):
        for j, symbol in enumerate(row):
            if symbol.isnumeric():
                total = total * 10 + int(symbol)
                gear_coordinates = gear_coordinates.union(adjacent_to_gear(schematic, i, j))

                if not (j + 1 < len(row) and row[j + 1].isnumeric()):

                    for coordinate in gear_coordinates:
                        if coordinate not in gears:
                            gears[coordinate] = []
                        gears[coordinate].append(total)
                    total = 0
                    gear_coordinates = set()
            else:
                total = 0
                gear_coordinates = set()

    result = 0
    for gear, values in gears.items():
        if len(values) == 2:
            result += values[0] * values[1]
    return result


if __name__ == "__main__":
    Solution(day3_main).solve()
    Solution(day3_bonus).solve()

from src.solution import Solution
from src.utils import split_by_empty_line, split_by_nextline


def parse_map(map_lines):
    map_data = [[int(s) for s in line.split(" ")] for line in split_by_nextline(map_lines)[1:]]

    def func(x):
        for line in map_data:
            if x in range(line[1], line[1] + line[2]):
                return x - line[1] + line[0]
        return x

    return func


def apply_all_maps(x, maps):
    for f in maps:
        x = f(x)
    return x


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def day5_main(input_string):
    # Parse
    lines = split_by_empty_line(input_string)
    seeds = [int(num) for num in lines[0].split(": ")[1].split(" ")]
    maps = [parse_map(m) for m in lines[1:]]

    return min([apply_all_maps(seed, maps) for seed in seeds])


def parse_seeds(seed_string):
    seeds = []
    for i, j in pairwise(seed_string):
        seeds.append((i, i + j))
    return seeds


def day5_bonus(input_string):
    lines = split_by_empty_line(input_string)
    seeds = parse_seeds([int(num) for num in lines[0].split(": ")[1].split(" ")])
    maps = [sorted([[int(x) for x in line.split(" ")] for line in split_by_nextline(ls)[1:]], key=lambda x: x[1]) for ls in lines[1:]]

    for m in maps:
        if m[0][1] != 0:
            m.insert(0, [0, 0, m[0][1]])
        a = m[-1][1]+m[-1][2]
        m.append([a, a, 9999999999])

    for m in maps:
        new_seeds = []
        for seed_range in seeds:
            for cond in m:
                x1 = cond[1]
                x2 = cond[1] + cond[2] - 1
                if seed_range[0] >= x1 and seed_range[1] <= x2:
                    a = cond[0] - cond[1]
                    new_seeds.append([seed_range[0] + a, seed_range[1] + a])
                elif x1 <= seed_range[0] <= x2:
                    a = cond[0] - cond[1]
                    new_seeds.append([seed_range[0] + a, x2 + a])
                elif x1 >= seed_range[0] and x2 <= seed_range[1]:
                    a = cond[0] - cond[1]
                    new_seeds.append([x1 + a, x2+ a])
                elif x1 <= seed_range[1] <= x2:
                    a = cond[0] - cond[1]
                    new_seeds.append([x1 + a, seed_range[1] + a])
                    break
        seeds = new_seeds

    return min(seeds, key=lambda x: x[0])


if __name__ == "__main__":
    Solution(day5_main).solve()
    Solution(day5_bonus).solve()

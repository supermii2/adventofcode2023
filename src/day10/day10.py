from src.solution import Solution
from src.utils import split_by_nextline

DIRECTIONS = {
    "|": (True, False, True, False),
    "-": (False, True, False, True),
    "L": (True, True, False, False),
    "J": (True, False, False, True),
    "F": (False, True, True, False),
    "7": (False, False, True, True),
    ".": (False, False, False, False)
}


def parse(s):
    return [list(x) for x in split_by_nextline(s)]


def inb(board, x, y):
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        return True
    else:
        return False


def find_valid_directions(board, x, y):
    if board[x][y] == "S":
        l = []
        return (
            inb(board, x - 1, y) and DIRECTIONS[board[x - 1][y]][2],
            inb(board, x, y + 1) and DIRECTIONS[board[x][y + 1]][3],
            inb(board, x + 1, y) and DIRECTIONS[board[x + 1][y]][0],
            inb(board, x, y - 1) and DIRECTIONS[board[x][y - 1]][1],
        )
    else:
        return DIRECTIONS[board[x][y]]


def find_s(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "S":
                return i, j


def day10_main(input_string):
    pipes = parse(input_string)
    visited = set()
    start = find_s(pipes)
    stack = [(start, 0)]
    m = 0

    while stack:
        current_node = stack.pop(0)
        visited.add(current_node[0])
        m = max(current_node[1], m)
        dirs = find_valid_directions(pipes, current_node[0][0], current_node[0][1])

        if dirs[0] and (current_node[0][0] - 1, current_node[0][1]) not in visited:
            stack.append(((current_node[0][0] - 1, current_node[0][1]), current_node[1] + 1))
        if dirs[1] and (current_node[0][0], current_node[0][1] + 1) not in visited:
            stack.append(((current_node[0][0], current_node[0][1] + 1), current_node[1] + 1))
        if dirs[2] and (current_node[0][0] + 1, current_node[0][1]) not in visited:
            stack.append(((current_node[0][0] + 1, current_node[0][1]), current_node[1] + 1))
        if dirs[3] and (current_node[0][0], current_node[0][1] - 1) not in visited:
            stack.append(((current_node[0][0], current_node[0][1] - 1), current_node[1] + 1))

    return m


def is_h_connected(left, right):
    return ((left == "F" or left == "-" or left == "L" or left == "S")
            and (right == "-" or right == "7" or right == "J" or right == "S"))


def is_v_connected(top, bottom):
    return ((top == "F" or top == "|" or top == "7" or top == "S") and
            (bottom == "J" or bottom == "|" or bottom == "L" or bottom == "S"))


def parse_bonus(s):
    s = split_by_nextline(s)
    l1 = []
    for i in range(len(s)):
        l2 = []
        for j in range(len(s[i])):
            l2.append(s[i][j])
            if j + 1 != len(s[i]) and is_h_connected(s[i][j], s[i][j + 1]):
                l2.append("-")
            elif j + 1 != len(s[i]):
                l2.append(".")
        l1.append(l2)
        l2 = []
        if i + 1 != (len(s)):
            for j in range(len(s[i])):
                if is_v_connected(s[i][j], s[i + 1][j]):
                    l2.append("|")
                else:
                    l2.append(".")
                if j + 1 != len(s[i]):
                    l2.append(".")
            l1.append(l2)
    return l1


def creep(board, x, y):
    if board[x][y] == "0":
        stack = [(x, y)]

        while stack:
            i, j = stack.pop()
            if inb(board, i - 1, j) and board[i - 1][j] == ".":
                board[i - 1][j] = "0"
                stack.append((i - 1, j))
            if inb(board, i + 1, j) and board[i + 1][j] == ".":
                board[i + 1][j] = "0"
                stack.append((i + 1, j))
            if inb(board, i, j + 1) and board[i][j + 1] == ".":
                board[i][j + 1] = "0"
                stack.append((i, j + 1))
            if inb(board, i, j - 1) and board[i][j - 1] == ".":
                board[i][j - 1] = "0"
                stack.append((i, j - 1))


def day10_bonus(input_string):
    pipes = parse(input_string)
    visited = set()
    start = find_s(pipes)
    stack = [(start, 0)]

    while stack:
        current_node = stack.pop(0)
        visited.add(current_node[0])
        dirs = find_valid_directions(pipes, current_node[0][0], current_node[0][1])

        if dirs[0] and (current_node[0][0] - 1, current_node[0][1]) not in visited:
            stack.append(((current_node[0][0] - 1, current_node[0][1]), current_node[1] + 1))
        if dirs[1] and (current_node[0][0], current_node[0][1] + 1) not in visited:
            stack.append(((current_node[0][0], current_node[0][1] + 1), current_node[1] + 1))
        if dirs[2] and (current_node[0][0] + 1, current_node[0][1]) not in visited:
            stack.append(((current_node[0][0] + 1, current_node[0][1]), current_node[1] + 1))
        if dirs[3] and (current_node[0][0], current_node[0][1] - 1) not in visited:
            stack.append(((current_node[0][0], current_node[0][1] - 1), current_node[1] + 1))

    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if (i, j) not in visited:
                pipes[i][j] = "."

    pipes = parse_bonus("\n".join(["".join(pipe) for pipe in pipes]))

    for i in range(len(pipes)):
        if pipes[i][0] == ".":
            pipes[i][0] = "O"
            creep(pipes, i, 0)
        if pipes[i][len(pipes[i]) - 1] == ".":
            pipes[i][len(pipes[i]) - 1] = "0"
            creep(pipes, i, len(pipes[i]) - 1)

    for j in range(len(pipes[0])):
        if pipes[0][j] == ".":
            pipes[0][j] = "0"
            creep(pipes, 0, j)
        if pipes[len(pipes) - 1][j] == ".":
            pipes[len(pipes) - 1][j] = "0"
            creep(pipes, len(pipes) - 1, j)

    c = 0
    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if pipes[i][j] == "." and i % 2 == 0 and j % 2 == 0:
                pipes[i][j] = "I"
                c += 1

    return c


if __name__ == "__main__":
    Solution(day10_main).solve()
    Solution(day10_bonus).solve()

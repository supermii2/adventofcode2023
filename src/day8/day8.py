import math

from src.solution import Solution
from src.utils import split_by_empty_line, split_by_nextline


class Node:
    def __init__(self, left_child, right_child):
        self.children = [left_child, right_child]


def day8_main(input_string):
    instruction_string, nodes_string = split_by_empty_line(input_string)
    instructions = [1 if ch == "R" else 0 for ch in list(instruction_string)]

    node_strings = split_by_nextline(nodes_string)
    node_dict = {}

    for node_string in node_strings:
        name, data = node_string.split(" = ")
        left_string, right_string = data[data.find("(") + 1:data.find(")")].split(", ")

        node_dict[name] = Node(left_string, right_string)

    current_node = "AAA"
    instruction_counter = 0
    num_instructions = len(instructions)

    while current_node != "ZZZ":
        instruction = instructions[instruction_counter % num_instructions]
        current_node = node_dict[current_node].children[instruction]
        instruction_counter += 1
    return instruction_counter


def day8_bonus(input_string):
    # The code for this is a mess because of numerous assumptions that had to be made of the problem
    # to make it solvable in a reasonable amount of time. These assumptions were not mentioned in the question.
    instruction_string, nodes_string = split_by_empty_line(input_string)
    instructions = [1 if ch == "R" else 0 for ch in list(instruction_string)]

    node_strings = split_by_nextline(nodes_string)
    node_dict = {}
    num_instructions = len(instructions)

    for node_string in node_strings:
        name, data = node_string.split(" = ")
        left_string, right_string = data[data.find("(") + 1:data.find(")")].split(", ")

        node_dict[name] = Node(left_string, right_string)

    remainders = []
    factors = []

    for node in node_dict:
        if node[-1] == 'A':
            instruction_counter = 0
            child_set = {}
            num_z = 0
            current_node = node
            while True:
                instruction = instructions[instruction_counter % num_instructions]
                if (current_node, instruction_counter % num_instructions) in child_set:
                    factors.append(instruction_counter
                                   - child_set[(current_node, instruction_counter % num_instructions)])
                    break
                child_set[(current_node, instruction_counter % num_instructions)] = instruction_counter
                current_node = node_dict[current_node].children[instruction]
                instruction_counter += 1
                if current_node[-1] == 'Z':
                    num_z += 1
                    remainders.append(instruction_counter)

    return math.lcm(*factors)


if __name__ == "__main__":
    Solution(day8_main).solve()
    Solution(day8_bonus).solve()

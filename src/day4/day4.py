from src.solution import Solution
from src.utils import split_by_nextline


class Card:
    winning_numbers: set[int]
    contained_numbers: set[int]
    memo: dict = dict()

    def __init__(self, id_num, winning_numbers, contained_numbers):
        self.id_num, self.winning_numbers, self.contained_numbers = id_num, winning_numbers, contained_numbers

    @classmethod
    def parse_card(cls, parse_string):
        id_string, data_string = parse_string.split(": ")
        id_num = int(id_string.split(" ")[-1]) - 1
        winning_num_string, contained_num_string = data_string.split(" | ")
        winning_numbers = {int(num) for num in winning_num_string.split(" ") if num != ""}
        contained_numbers = {int(num) for num in contained_num_string.split(" ") if num != ""}
        return cls(id_num, winning_numbers, contained_numbers)

    def find_num_matches(self):
        if self.id_num in Card.memo:
            return Card.memo[self.id_num]

        num = len(self.winning_numbers.intersection(self.contained_numbers))
        Card.memo[self.id_num] = num
        return num

    def calculate_score(self):
        size = len(self.winning_numbers.intersection(self.contained_numbers))
        return 2 ** (size - 1) if size > 0 else 0


def day4_main(input_string):
    cards = split_by_nextline(input_string)
    score = [Card.parse_card(card).calculate_score() for card in cards]
    return sum(score)


def day4_bonus(input_string):
    cards = [[Card.parse_card(card), 1] for card in split_by_nextline(input_string)]
    for card, num_cards in cards:
        matches = card.find_num_matches()
        for i in range(matches):
            cards[i + card.id_num + 1][1] += num_cards

    return sum([card[1] for card in cards])


if __name__ == "__main__":
    Solution(day4_main).solve()
    Solution(day4_bonus).solve()

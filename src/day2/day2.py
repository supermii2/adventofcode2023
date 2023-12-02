from src.solution import Solution
from src.utils import split_by_nextline


class Round:
    num_red: int = 0
    num_green: int = 0
    num_blue: int = 0

    @classmethod
    def parse(cls, rnd_str: str):
        rnd = cls()
        terms = rnd_str.split(", ")
        for term in terms:
            num_str, color = term.split(" ")
            if color == 'red':
                rnd.num_red = int(num_str)
            if color == 'green':
                rnd.num_green = int(num_str)
            if color == 'blue':
                rnd.num_blue = int(num_str)
        return rnd

    def is_valid_round(self, red_limit, green_limit, blue_limit):
        return not (self.num_red > red_limit or self.num_green > green_limit or self.num_blue > blue_limit)


class Game:
    id: int
    rounds: list[Round] = []

    @classmethod
    def parse(cls, game: str):
        result = cls()
        game_id, game_data = game.split(": ")
        result.id = int(game_id.split(" ")[1])
        result.rounds = [Round.parse(rnd) for rnd in game_data.split("; ")]
        return result

    def is_valid_game(self, num_red, num_green, num_blue):
        return all([rnd.is_valid_round(num_red, num_green, num_blue) for rnd in self.rounds])

    def power(self):
        min_red, min_green, min_blue = 0, 0, 0
        for rnd in self.rounds:
            if rnd.num_red > min_red:
                min_red = rnd.num_red
            if rnd.num_green > min_green:
                min_green = rnd.num_green
            if rnd.num_blue > min_blue:
                min_blue = rnd.num_blue
        return min_red * min_green * min_blue


def day2_main(input_string):
    games = [Game.parse(game) for game in split_by_nextline(input_string)]
    return sum([game.id for game in games if game.is_valid_game(12, 13, 14)])


def day2_bonus(input_string):
    games = [Game.parse(game) for game in split_by_nextline(input_string)]
    return sum([game.power() for game in games])


if __name__ == "__main__":
    Solution(day2_main).solve()
    Solution(day2_bonus).solve()

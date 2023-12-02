from src.solution import Solution
from src.utils import split_by_nextline


# This was written in a rush, could probably be made much more cleanly with an object oriented approach

def parse_game(game_string: str) -> dict:
    lowest_red, lowest_green, lowest_blue = 0, 0, 0
    parsed_game = {}
    game_id, game_data = game_string.split(": ")
    parsed_game['id'] = int(game_id.split(" ")[1])
    parsed_game['sets'] = []

    for rnd in game_data.split("; "):
        terms = {}
        for term in rnd.split(", "):
            num_str, color = term.split(" ")
            num = int(num_str)
            if color == 'red' and lowest_red < num:
                lowest_red = num
            if color == 'green' and lowest_green < num:
                lowest_green = num
            if color == 'blue' and lowest_blue < num:
                lowest_blue = num
            terms[color] = int(num_str)

        parsed_game['sets'].append(terms)
    parsed_game['power'] = lowest_blue * lowest_red * lowest_green
    return parsed_game


def is_valid_game(game):
    num_red, num_green, num_blue = 12, 13, 14
    for rnd in game['sets']:
        for color, num in rnd.items():
            if color == 'red' and num > num_red:
                return False
            if color == 'green' and num > num_green:
                return False
            if color == 'blue' and num > num_blue:
                return False
            if color != 'red' and color != 'green' and color != 'blue':
                return False
    return True


def day2_main(input_string):
    games = [parse_game(game) for game in split_by_nextline(input_string)]
    filtered_games = [game for game in games if is_valid_game(game)]
    for game in filtered_games:
        print(game)
    return sum([game['id'] for game in filtered_games])


def day2_bonus(input_string):
    return sum([parse_game(game)['power'] for game in split_by_nextline(input_string)])


if __name__ == "__main__":
    Solution(day2_main).solve()
    Solution(day2_bonus).solve()

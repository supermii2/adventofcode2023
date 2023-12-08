import collections
import functools

from src.solution import Solution

from enum import Enum

from src.utils import split_by_nextline


class HandTypes(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


def getHandType(hand):
    c = collections.Counter(hand)
    if len(c) == 1:
        return HandTypes.FIVE_OF_A_KIND
    elif c.most_common(1)[0][1] == 4:
        return HandTypes.FOUR_OF_A_KIND
    elif len(c) == 2:
        return HandTypes.FULL_HOUSE
    elif c.most_common(1)[0][1] == 3:
        return HandTypes.THREE_OF_A_KIND
    elif [x[1] for x in c.most_common(2)] == [2, 2]:
        return HandTypes.TWO_PAIR
    elif c.most_common(1)[0][1] == 2:
        return HandTypes.ONE_PAIR
    else:
        return HandTypes.HIGH_CARD


def getHandTypeBonus(hand):
    c = collections.Counter(hand)
    c_no_joker = collections.Counter(hand.replace("J", ""))
    if len(c_no_joker) <= 1 or len(c) == 2 and c['J'] != 0:
        return HandTypes.FIVE_OF_A_KIND
    elif c.most_common(1)[0][1] == 4 or c_no_joker.most_common(1)[0][1] + c['J'] == 4:
        return HandTypes.FOUR_OF_A_KIND
    elif len(c) == 2 or len(c) == 3 and c['J'] != 0:
        return HandTypes.FULL_HOUSE
    elif c.most_common(1)[0][1] == 3 or c_no_joker.most_common(1)[0][1] + c['J'] == 3:
        return HandTypes.THREE_OF_A_KIND
    elif ([x[1] for x in c.most_common(2)] == [2, 2] or c_no_joker.most_common(1)[0][1] == 2 and c['J'] == 1 or
          c['J'] >= 2):
        return HandTypes.TWO_PAIR
    elif c.most_common(1)[0][1] == 2 or c['J'] >= 1:
        return HandTypes.ONE_PAIR
    else:
        return HandTypes.HIGH_CARD


CARD_ORDERS = "23456789TJQKA"
CARD_ORDERS_BONUS = "J23456789TQKA"


def compare_hands(hand1, hand2, bonus):
    ht1, ht2 = (getHandTypeBonus(hand1), getHandTypeBonus(hand2)) if bonus else (getHandType(hand1), getHandType(hand2))
    order = CARD_ORDERS_BONUS if bonus else CARD_ORDERS
    if ht1 > ht2:
        return 1
    elif ht1 < ht2:
        return -1
    else:
        while hand1 != "":
            if order.index(hand1[0]) > order.index(hand2[0]):
                return 1
            elif order.index(hand1[0]) < order.index(hand2[0]):
                return -1
            else:
                hand1 = hand1[1:]
                hand2 = hand2[1:]

        return 0


def day7_main(input_string):
    hand_bid_pairs = [x.split(" ") for x in split_by_nextline(input_string)]
    sorted_hand_bid_pairs = sorted(hand_bid_pairs, key=functools.cmp_to_key(lambda x, y: compare_hands(x[0], y[0], False)))
    return sum([(i + 1) * int(x[1]) for i, x in enumerate(sorted_hand_bid_pairs)])


def day7_bonus(input_string):
    hand_bid_pairs = [x.split(" ") for x in split_by_nextline(input_string)]
    sorted_hand_bid_pairs = sorted(hand_bid_pairs, key=functools.cmp_to_key(lambda x, y: compare_hands(x[0], y[0], True)))
    return sum([(i + 1) * int(x[1]) for i, x in enumerate(sorted_hand_bid_pairs)])


if __name__ == "__main__":
    Solution(day7_main).solve()
    Solution(day7_bonus).solve()

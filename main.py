from math import ceil, floor
from random import randint
from operator import itemgetter

def get_game_turns(sides, probability_order):
    game_turns = 0

    position = [False] * 2 * sides

    while not check_game_end(position, (sides * 2) - 1):
        roll_1 = randint(1, sides)
        roll_2 = randint(1, sides)
        roll_sum = roll_1 + roll_2

        card_to_flip = get_optimal_move([roll_1, roll_2, roll_sum], position, probability_order)

        position[card_to_flip] = not position[card_to_flip]

        game_turns += 1

        #print([roll_1, roll_2, roll_sum])

        #print(position)

    return game_turns


def get_optimal_move(rolls, position, probability_order):
    card_indices = [rolls[0] - 1, rolls[1] - 1, rolls[2] - 1]

    if False in list(itemgetter(*card_indices)(position)):
        return find_card_to_flip(rolls, probability_order, position, False)

    else:
        return find_card_to_flip(rolls, probability_order[::-1], position, True)


def find_card_to_flip(rolls, probability_order, position, position_target):
    for card in probability_order:
        if card in rolls and position[card-1] == position_target:
            return card - 1



def check_game_end(position, sum_count):
    if False not in position:
        return True

    else:
        return False

def get_probability_order(sides): # Not correct
    lower_results = list(range(1, ceil(sides / 2) + 1))
    upper_results = list(range(sides, sides - floor(sides / 2), -1))

    ordered_results  = [None]*(len(lower_results) + len(upper_results))
    ordered_results[::2] = lower_results
    ordered_results[1::2] = upper_results

    return ordered_results


def get_expected_turns(sides):
    #probability_order = get_probability_order(2 * sides)
    probability_order = [4, 3, 1, 2] # list(range(12, 6, -1)) + list(range(1, 7))

    total_turns = 0

    for game in range(100000000):
        total_turns += get_game_turns(sides, probability_order)

    return total_turns / 100000000


print(get_expected_turns(2))

#print(get_optimal_move([1, 1, 2], [True, False, True, True], [4, 3, 1, 2]))


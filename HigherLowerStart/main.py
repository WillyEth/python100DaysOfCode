import random

from HigherLowerStart.art import logo, vs
from HigherLowerStart.game_data import data

DATA_LENGTH = len(data)

end_game = False


def get_random():
    """
    Get a random number based on the data dictionary
    :rtype: int
    """
    return random.randint(0, DATA_LENGTH)


def check_choice(a1: int, b1: int):
    """
    check choice end game
    :param a1:
    :param b1:
    :return:
    """
    choice = input("Who has more followers? Type 'A' or 'B'  ").lower()
    print(f"my choice {choice}")
    correct_answer = ""
    if a1 > b1:
        correct_answer = "a"
    else:
        correct_answer = "b"

    if choice == correct_answer:
        print(f"Correct Keep Going")
        return False
    else:
        print(f"Wrong Game Ending")
        return True


pick_one = get_random()
score: int = 0
while not end_game:
    pick_two = get_random()
    print(logo)
    a_int = data[pick_one]['follower_count']
    b_int = data[pick_two]['follower_count']
    print(f"Compare A: {data[pick_one]['name']}, {data[pick_one]['description']}, from {data[pick_one]['country']}")
    print(vs)
    print(f"Compare B: {data[pick_two]['name']}, {data[pick_two]['description']}, from {data[pick_two]['country']}")

    print(a_int)
    print(b_int)
    pick_one = pick_two
    end_game = check_choice(a_int, b_int)
    pick_one = pick_two

    score = score + 1

    print(f"Score = {score}")

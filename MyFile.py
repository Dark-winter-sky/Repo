from random import randint


def generate_two_random_numbers():
    random_number_a = randint(1, 10)
    random_number_b = randint(1, 10)
    return random_number_a, random_number_b


def prompt_user_for_product(number_a, number_b):
    return input("What is the product of " + str(number_a) + " and " + str(number_b) + "? ")


def mark_answer(answer, number_a, number_b, score):
    if answer == number_a * number_b:
        result = "correct"
    else:
        result = "incorrect"

    return result


def determine_score(result, score):
    if result == "correct":
        score += 1
    else:
        score -= 1

    return score


def print_score(result, score):
    if result == "correct":
        print("Correct! Your score is " + str(score))
    else:
        print("Incorrect. Your score is " + str(score))


def add_missing_line_break():
    print("\n")


def play_game():
    score = 0
    play = "y"
    new_repetition = False
    welcome_message = "\nLet's play a multiplication game!\n"

    print(welcome_message)

    while play == "y":
        if new_repetition:
            add_missing_line_break()
            print(welcome_message)
        number_a = generate_two_random_numbers()[0]
        number_b = generate_two_random_numbers()[1]
        answer = int(prompt_user_for_product(number_a, number_b))
        result = mark_answer(answer, number_a, number_b, score)
        score = determine_score(result, score)
        print_score(result, score)
        play = input("Do you want to play again? (y/n) ")
        new_repetition = True


play_game()

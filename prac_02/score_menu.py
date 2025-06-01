def main():
    score = get_valid_score()

    MENU = """\nMenu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

    choice = ''
    while choice != 'Q':
        print(MENU)
        choice = input(">>> ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(get_result(score))
        elif choice == 'S':
            print_stars(score)
        elif choice == 'Q':
            print("Farewell! Thanks for using the program.")
        else:
            print("Invalid option, please try again.")


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while not (0 <= score <= 100):
        print("Score must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def print_stars(score):
    print('*' * int(score))

main()

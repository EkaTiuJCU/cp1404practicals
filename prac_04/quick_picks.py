import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    numbers = int(input("How many quick picks? "))
    for _ in range(numbers):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))

def generate_quick_pick():
    picked = []
    while len(picked) < NUMBERS_PER_LINE:
        num = random.randint(MINIMUM, MAXIMUM)
        if num not in picked:
            picked.append(num)
    picked.sort()
    return picked

main()

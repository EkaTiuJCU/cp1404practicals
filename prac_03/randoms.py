import random

print(random.randint(5, 20))  # line 1
# Expected range: inclusive of both 5 and 20
# Smallest number: 5
# Largest number: 20

print(random.randrange(3, 10, 2))  # line 2
# Expected values: 3, 5, 7, 9 (step of 2 from 3 up to but not including 10)
# Smallest number: 3
# Largest number: 9
# Could it produce a 4? No, because 4 is not part of the sequence with step 2 from 3

print(random.uniform(2.5, 5.5))  # line 3
# Produces a float between 2.5 and 5.5
# Smallest number: approx. 2.5
# Largest number: approx. 5.5

random_number = random.randint(1, 100)
print(random_number)

"""names_to_age = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}

for name, age in sorted(names_to_age.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} = {age}")"""

strings = ["red", "white", "blue"]

def main(strings):
    result = {strings: len(strings) for strings in strings}
    print(result)

main(strings)

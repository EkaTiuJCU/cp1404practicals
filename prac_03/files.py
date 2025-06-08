out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
    print(total)

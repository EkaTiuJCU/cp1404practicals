name = "Gibson L-5 CES"
year = 1922
cost = 16035.999

print("My guitar: {} {}".format(year, name))
print("My guitar: {1} {0}".format(name, year))
print("My guitar: {0} {0} {0}".format(name))
print("My guitar: {} for about ${:,.2f}!".format(name, cost))

print(f"My guitar: {year} {name}")
print(f"My guitar: {name} for about ${cost:,.2f}!")

numbers = [1, 19, 123456, 4, 987]
for i in numbers:
    print(f"Number is {i:>10}")

print(f"{year} {name} for about ${cost:,.0f}!")

for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

print("My guitar: " + name + ", first made in " + str(year))

print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

print(f"My {name} was first made in {year} (that's right, {year}!)")

print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

print(f"{year} {name} for about ${cost:,.0f}!")

for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
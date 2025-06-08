try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (not zero): "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Please enter a non-zero denominator: "))
    result = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid integers!")
else:
    print(f"Result is {result}")
print("Finished.")
is_finished = False
while not is_valid_input:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")

print(f"Valid result is: {result}")
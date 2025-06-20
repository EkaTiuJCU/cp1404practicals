COLOUR_CODES = {"aliceblue": "#f0f8ff","antiquewhite": "#faebd7",
                "aqua": "#00ffff","aquamarine": "#7fffd4","azure":
                "#f0ffff","beige": "#f5f5dc","bisque": "#ffe4c4",
                "black": "#000000","blanchedalmond": "#ffebcd",
                "blue": "#0000ff"}

def main():
    while True:
        colour_name = input("Enter a colour name (or blank to quit): ").lower()
        if colour_name == "":
            break
        hex_code = COLOUR_CODES.get(colour_name)
        if hex_code:
            print(f"The hex code for {colour_name} is {hex_code}")
        else:
            print(f"Sorry, '{colour_name}' is not a known colour name.")

main()

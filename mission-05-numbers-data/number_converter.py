# number_converter.py
# A small program that converts a decimal number to binary and hexadecimal.

def main():
    user_input = input("Enter a positive decimal number: ")
    number = int(user_input)

    binary_result = bin(number)       # Converts to binary string, e.g. '0b1101'
    hex_result = hex(number)          # Converts to hexadecimal string, e.g. '0xd'

    print(f"Decimal: {number}")
    print(f"Binary:  {binary_result}")
    print(f"Hexadecimal: {hex_result}")

if __name__ == "__main__":
    main()

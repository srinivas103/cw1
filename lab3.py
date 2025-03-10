import sys

def decimal_to_hex(decimal_value):
    """Converts a decimal number to its hexadecimal equivalent."""
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    if num == 0:
        return "0"  # Special case for zero

    while num > 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return the hexadecimal value for testing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <decimal_number>")
        sys.exit(1)

    try:
        decimal_value = int(sys.argv[1])
        if decimal_value < 0:
            print("Error: Please provide a non-negative integer.")
            sys.exit(1)
        
        decimal_to_hex(decimal_value)
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)

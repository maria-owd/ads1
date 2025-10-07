def count_bits(number):
    """Counts the number of bits set to 1 in the binary representation of a number using bitwise operations."""
    count = 0
    while number:
        lastBit = number & 1
        # print(lastBit)
        count += lastBit
        # Right shift the number to process the next bit
        number >>= 1
    return count

def main():
    print("Welcome to the Bit Counter!")
    try:
        user_input = int(input("Enter an integer: "))
        bit_count = count_bits(user_input)
        print(f"The number {user_input} has {bit_count} bits set to 1 in its binary representation.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

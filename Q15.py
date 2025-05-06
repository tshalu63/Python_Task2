def reverse_number(num):
    rev = int(str(num)[::-1])  # Convert to string, reverse, then convert back to int
    return rev

print("Reversed:", reverse_number(2314))  # Should output: Reversed: 4132
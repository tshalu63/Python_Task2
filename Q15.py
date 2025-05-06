def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

# Example
print("Reversed:", reverse_number(2314))  # 4132
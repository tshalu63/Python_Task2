def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

# Example
print("Number of digits:", count_digits(123456))  # Output: 6
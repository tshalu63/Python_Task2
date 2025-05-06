def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
print("GCD is:", gcd(36, 60))  # 12
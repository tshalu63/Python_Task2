def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d ** power for d in digits)


print("Is Armstrong:", is_armstrong(153))  # True
def sum_divisible_by_3_or_5(limit):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)


print("Sum:", sum_divisible_by_3_or_5(100))  
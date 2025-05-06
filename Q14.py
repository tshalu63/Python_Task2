def print_special_numbers():
    for i in range(1, 101):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=' ')


print_special_numbers()
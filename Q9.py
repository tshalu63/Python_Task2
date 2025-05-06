def get_positive_number():
    while True:
        try:
            num = int(input("Enter a number > 0: "))
            if num > 0:
                print("Valid number:", num)
                break
            else:
                print("Number must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

# Uncomment to run:
# get_positive_number()
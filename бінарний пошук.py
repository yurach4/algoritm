def binary_search(min_limit, max_limit, count=0):
    middle = (min_limit + max_limit) // 2

    question = input(
        f"I think your number is: {middle}. Is this your number or not?\n"
        f"If yes, enter 'yes'. If no, enter 'lower' or 'upper':\n"
    ).lower()

    if question == "yes":
        return f"Your number was found in {count} tries!"
    elif question == "upper":
        count += 1
        return binary_search(middle + 1, max_limit, count)
    elif question == "lower":
        count += 1
        return binary_search(min_limit, middle - 1, count)
    else:
        print("Please enter a valid response: 'yes', 'lower', or 'upper'.")
        return binary_search(min_limit, max_limit, count)


min_limit = int(input("Enter the lower limit:\n"))
max_limit = int(input("Enter the upper limit:\n"))
print(binary_search(min_limit, max_limit))

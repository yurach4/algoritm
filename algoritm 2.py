def sorting_algorithm_2(list_of_numbers):
    length = len(list_of_numbers)
    for i in range(length):
        for j in range(0, length - i - 1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
    return list_of_numbers

def sorting_algorithm_1(list_of_numbers):
    new_list = []
    while list_of_numbers:
        min_value = min(list_of_numbers)
        new_list.append(min_value)
        list_of_numbers.remove(min_value)
    return new_list

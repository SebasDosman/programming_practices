def list_comprehension_excercise():
    values = '32,45,11,87,20,48'
    new_values = values.split(',')

    combinations = [f'{ v1 }x{ v2 }' for v1 in new_values for v2 in new_values]
    print(combinations)

    new_combinations = [f'{ v1 }x{ v2 }={ int(v1) * int(v2) }' for v1 in new_values for v2 in new_values if (int(v1) * int(v2)) % 2 != 0]
    print(new_combinations)

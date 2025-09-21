def remove_elements(list_to_remove_elements):
    indices_a_remover = {0, 4, 5}
    return [elem for i, elem in enumerate(list_to_remove_elements) if i not in indices_a_remover]

print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))


def add_elements(list_to_add_elements):
    return ["Pink"] + list_to_add_elements + ["Yellow"]

print(add_elements(['Red', 'Green', 'White', 'Black']))


def is_empty(list_to_check):
    return len(list_to_check) == 0

print(is_empty([]))
print(is_empty([1, 2]))


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    return False

print(check_lists(['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White'],
                  ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']))

print(check_lists(['Black', 'Pink', 'Green', 'White'],
                  ['Red', 'Green', 'Yellow', 'Black', 'Pink']))


def list_of_lists(list_of_lists_to_modify):
    result = []

    # primera lista → primeros 2 elementos
    if len(list_of_lists_to_modify[0]) >= 2:
        result.append(list_of_lists_to_modify[0][:2])
    else:
        result.append(list_of_lists_to_modify[0])

    # segunda lista → elementos entre índice 1 y 3 (inclusive)
    if len(list_of_lists_to_modify[1]) >= 4:
        result.append(list_of_lists_to_modify[1][1:4])
    else:
        result.append(list_of_lists_to_modify[1][1:])

    # tercera lista → últimos 2 elementos
    if len(list_of_lists_to_modify[2]) >= 2:
        result.append(list_of_lists_to_modify[2][-2:])
    else:
        result.append(list_of_lists_to_modify[2])

    return result

print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))

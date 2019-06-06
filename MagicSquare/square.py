def give_me_square(magic_number):
    return 0

def sum_rows(square: list):
    total = sum(square[0])

    for row in square[1:]:
        if total != sum(row):
            return -1

    return total

def sum_columns(square: list):
    total = sum(square[0])

    for row in square[1:]:
        if total != sum(row):
            return -1

    return total


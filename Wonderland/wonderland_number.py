# Info and definition on https://github.com/gigasquid/wonderland-clojure-katas/tree/master/wonderland-number

# Here I will use it as a list of numbers
def find_number_list_nested_loop():
    # Starts from 100000 and ends on 166666 (999999/6)
    numbers = [0,0,0,0,0,0]

    for first in range (1,2):
        for second in range (0,10):
            for third in range (0,10):
                for fourth in range (0,10):
                    for fifth in range (0,10):
                        for sixth in range (0,10):
                            numbers = [first, second, third, fourth, fifth, sixth]
                            if not same_digits(numbers, multiply_and_return_list(numbers, 2)):
                                continue
                            if not same_digits(numbers, multiply_and_return_list(numbers, 3)):
                                continue
                            if not same_digits(numbers, multiply_and_return_list(numbers, 4)):
                                continue
                            if not same_digits(numbers, multiply_and_return_list(numbers, 5)):
                                continue
                            if not same_digits(numbers, multiply_and_return_list(numbers, 6)):
                                continue
                            
                            # If we get here, we found it
                            return "".join(str(e) for e in numbers)

    return "".join(str(e) for e in numbers)

def same_digits(number: list, toCompare: list):
    copy_number = number.copy()
    copy_compare = toCompare.copy()

    copy_compare.sort()
    copy_number.sort()

    return copy_compare == copy_number

def multiply_and_return_list(number: list, multiply: int):
    int_number = int("".join(str(e) for e in number))
    new_list = [int(i) for i in str(int_number * multiply)]

    if len(new_list) < 6:
        new_list.insert(0,0)

    return new_list
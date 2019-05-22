# First implementation. It found an infinite loop when searching for something in between. Fixed by setting the first direction
def search_iterative(number: int, array: list):

    half = len(array) // 2
    index = half

    found = -1

    while index in range(0, len(array)):
        element = array[index]
        if element == number:
            found = index
            break

        if element < number:
            # If we took a turn
            if index < half:
                break
            index = index + 1

        if element > number:
            # If we took a turn
            if index > half:
                break
            index = index - 1

    return found

# Doing half jumps all the time. Problem is returning the right index
def search_recursive(number: int, array: list, index=0):
    if array == []:
        return -1
    
    half = len(array) // 2

    element = array[half]

    found = -1

    if number == element:
        return half
    elif half == 0:
        return -1
    
    if number < element:
        found = search_recursive(number, array[:half])
    else:
        found = search_recursive(number, array[half:])
        if found > -1:
            found = found + half
        

    return found


def search_python(number: int, array: list):
    try:
        index = array.index(number)
    except:
        index = -1

    return index

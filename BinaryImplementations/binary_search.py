# First implementation. It found an infinite loop when searching for something in between. Fixed by setting the first direction
def search_iterative(number: int, array: list):

    half = len(array) // 2
    index = half

    found = -1

    while index in range(0,len(array)):
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

def searchPython(number:int, array:list):
    try:
        index = array.index(number)
    except:
        index = -1

    return index
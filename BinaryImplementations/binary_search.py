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

# Doing half jumps all the time. Problem is returning the right index, solved by adding the different halves


def search_recursive(number: int, array: list):
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

#It is slower than recursive so... I'm creating too much overhead. Having something recursive in a thread is not a good idea.
def search_thread(number: int, array: list):
    def run(number: int, array: list, starting_index: int):
        if array == []:
            return -1

        half = len(array) // 2

        element = array[half]

        found = -1

        if number == element:
            return starting_index + half
        elif half == 0:
            return -1

        if number < element:
            found = search_recursive(number, array[:half])
        else:
            found = search_recursive(number, array[half:])
            if found > -1:
                found = found + half

        return starting_index + found

    if array == []:
            return -1

    maximum_threads = 8

    num_threads = len(array) if len(array) < 8 else maximum_threads

    new_size = len(array) // num_threads

    from multiprocessing.pool import ThreadPool
    pool = ThreadPool(processes=num_threads)

    results = []
    for i in range(num_threads):
        starting_index = new_size * i
        end_index = new_size * (i+1)
        result = pool.apply_async(
            run, (number, array[starting_index:end_index], starting_index))
        results.append(result)

    for result in results:
        value = result.get()
        if value > -1:
            return value

    return -1


def search_python(number: int, array: list):
    try:
        index = array.index(number)
    except:
        index = -1

    return index

def find_pair(numbers: list, target: int): 

    lowest_pair_index = len(numbers)
    lowest_pair = None

    sorted_numbers = numbers
    sorted_numbers.sort()

    index = 1

    for x in sorted_numbers[0:-1]:

        if (x >= target):
            break

        print ("First number is " + str(x) + " from " + str(sorted_numbers[0:-1]))
        # We only care if it's below the target

        for y in sorted_numbers[index:]:

            print("I am testing " + str(y) + " from " + str(sorted_numbers[index:]))
            if (x + y > target):
                break
            
            if (x + y == target):

                # This way it allows me to get the index for the two elements, even if they are the same
                index_x = numbers.index(x)
                pair_index = index_x - numbers.index(y, index_x) * -1

                print("pair is " + str([x,y]) + " with index " + str(pair_index))
                if (pair_index < lowest_pair_index):
                    lowest_pair_index = pair_index
                    lowest_pair = [x, y]
                
                break          

        index = index + 1

    return lowest_pair


def find_pair_pretty(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
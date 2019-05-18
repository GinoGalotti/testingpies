# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.


# As this doesn't require to carry the state,
# I'm going to do it as an static class

# Ways to optimize it:
#  When call with -2 to 5, we only have to sum 3+4+5. So having a positive and negative number, we only care about the difference of the absolutes with the sign of the biggest

def get_sum(a: int, b: int):

    # I'll use array methods to order it easier, and to use native libraries for adding it

    numbers = [a, b]

    numbers.sort()

    delta = numbers[1] - numbers[0]

    # When it's the same number
    if delta == 0:
        return numbers[0]

    if (delta > 1):
        i = 1
        while i < delta:
            numbers.append(numbers[0] + i)
            i = i + 1

    return sum(numbers)

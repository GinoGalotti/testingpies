#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]



# As this doesn't require to carry the state, 
# I'm going to do it as an static class

# Ways to optimize it:
#  When call with -2 to 5, we only have to sum 3+4+5. So having a positive and negative number, we only care about the difference of the absolutes with the sign of the biggest

def move(elements: list):
    
    # ocurrences = elements.count(0)

    # if ocurrences:
    #     elements = delete_zeroes(elements)
    #     # Append the zeroes at the end
    #     elements.extend([0]*ocurrences)

    # This is a more elegant solution, I always forget to use Lambdas
    return sorted(elements, key=lambda x: x is 0)

def delete_zeroes(elements: list):
    while elements.count(0):
        elements.remove(0) 
    return elements
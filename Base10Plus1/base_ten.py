def add_one(digits: list):
    # I wanted to reverse the list, but that has o(n) complexity and it's not really needed, instead we will use the non-python way of using an index
    last_index = len(digits)-1
    carry = 0 # Will allow us to understand when to carry one

    # Add one to the last
    digits[last_index] = digits[last_index] + 1

    for x in range(last_index, -1, -1):
        number = digits[x]
        if carry:
            number = number + carry
            carry = 0
        if number > 9:
            number = number % 10
            carry = 1
        digits[x] = number
        
        # We don't need to continue if we're not carrying anything
        if not carry:
            break

    # if we have carry at the end, it means we're in the overflow scenario

    if carry:
        digits.insert(0, 1)

    return digits

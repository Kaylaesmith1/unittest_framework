def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
# return True use when testing functions    
    if isinstance(numbers, list):
        # write a test that fails (return True below)
        # return True
        # then write a test that passes (if numbers... return False)
        # if numbers == []:
        #     return False
        # else:
            # Follow the DRY (dont repeat yourself) method. the 'if numbers.. else' above is repetitive bc it's covered below with evens = 0. 
        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False
        
        # we can replace evens = 0 above with sum from below and delete the rest of the repetitive code.
        # print(sum([1 for n in numbers if n % 2 == 0]))

        # for n in numbers:
        #     if n % 2 == 0:
        #         evens += 1
        # if evens:
        #     return evens % 2 == 0
        # else:
        #     return False
    else:
        raise TypeError('A list was not passed into the funciton.')


if __name__ == '__main__':
    even_number_of_evens([2, 1, 4])

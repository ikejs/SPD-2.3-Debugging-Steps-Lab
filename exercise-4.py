"""
Exercise 4
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by 
        performing a binary search.
    """
    if high == None:
        high = len(arr)

    if high >= low: 
        mid = (high + low) // 2

        if arr[mid] == element: 
            return mid 
        elif arr[mid] > element: 
            return binary_search(arr, element, low, mid - 1) 
        else: 
            return binary_search(arr, element, mid + 1, high) 

    else: 
        return -1


if __name__ == '__main__':
    print('### Binary Sort ###')
    answer = binary_search([1, 2, 4, 5, 7, 10, 11], 10)
    print(answer)
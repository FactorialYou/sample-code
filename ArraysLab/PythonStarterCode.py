def number_of_elements(array):
    """
    Returns the number of elements in the array.

    Examples:
    >>> number_of_elements([5, 3, 2])
    3
    >>> number_of_elements([])
    0
    >>> number_of_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    10
    """
    pass  # TODO: Implement this function


def first_element(array):
    """
    Returns the first element in the array.

    Examples:
    >>> first_element([5, 3, 2])
    5
    >>> first_element([9, 6, 4])
    9
    >>> first_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    0
    """
    pass  # TODO: Implement this function


def last_element(array):
    """
    Returns the last element in the array.

    Examples:
    >>> last_element([5, 3, 2])
    2
    >>> last_element([9, 6, 4])
    4
    >>> last_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    9
    """
    pass  # TODO: Implement this function


def nth_element(array, n):
    """
    Returns the nth element in the array.

    Parameters:
    array (list): The list of integers.
    n (int): The index of the element to retrieve.

    Examples:
    >>> nth_element([5, 3, 2], 1)
    3
    >>> nth_element([9, 6, 4], 0)
    9
    >>> nth_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
    6
    """
    pass  # TODO: Implement this function

def first_times_last(array):
    """
    Returns the product of the first and last elements in the array.

    Examples:
    >>> first_times_last([5, 3, 2])
    10
    >>> first_times_last([9, 6, 4])
    36
    >>> first_times_last([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    0
    """
    pass  # TODO: Implement this function


def middle_element(array):
    """
    Returns the middle element in the array.

    Examples:
    >>> middle_element([5, 3, 2])
    3
    >>> middle_element([9, 6, 4])
    6
    >>> middle_element([0, 1, 2, 3, 4, 5])
    2
    """
    pass  # TODO: Implement this function


def number_of_even_elements(array):
    """
    Returns the number of even numbers in the array.

    Examples:
    >>> number_of_even_elements([5, 3, 7])
    0
    >>> number_of_even_elements([9, 6, 4])
    2
    >>> number_of_even_elements([0, 1, 2, 3, 4, 5])
    3
    """
    pass  # TODO: Implement this function


def double_elements(array):
    """
    Doubles every value in the array and returns the updated array.

    Examples:
    >>> double_elements([5, 3, 7])
    [10, 6, 14]
    >>> double_elements([9, 6, 4])
    [18, 12, 8]
    >>> double_elements([0, 1, 2])
    [0, 2, 4]
    """
    pass  # TODO: Implement this function

def one_to_n(n):
    """
    Creates an array of elements from 1 to n and returns it.

    Examples:
    >>> one_to_n(3)
    [1, 2, 3]
    >>> one_to_n(5)
    [1, 2, 3, 4, 5]
    >>> one_to_n(1)
    [1]
    """
    pass  # TODO: Implement this function


def array_slice(array, a, b):
    """
    Returns a new array containing all values of `array` between position `a` and up to but not including `b`.

    Examples:
    >>> array_slice([5, 3, 2, 1, 7, 0], 1, 3)
    [3, 2]
    >>> array_slice([9, 6, 4, 9, 6, 4], 2, 6)
    [4, 9, 6, 4]
    >>> array_slice([0, 1, 2, 3, 4, 5], 0, 3)
    [0, 1, 2]
    """
    pass  # TODO: Implement this function


def sum_of_elements(array):
    """
    Returns the sum of all the numbers in the array.

    Examples:
    >>> sum_of_elements([1, 2, 3])
    6
    >>> sum_of_elements([9, 6, 4])
    19
    >>> sum_of_elements([0, 0, 0])
    0
    """
    pass  # TODO: Implement this function


def average_of_elements(array):
    """
    Returns the average of all the numbers in the array.

    Examples:
    >>> average_of_elements([1, 2, 3])
    2
    >>> average_of_elements([9, 6, 3])
    6
    >>> average_of_elements([1, 1, 1])
    1
    """
    pass  # TODO: Implement this function

def smallest_to_largest(array):
    """
    Returns the elements in the array ordered from smallest to largest.

    Examples:
    >>> smallest_to_largest([2, 3, 1])
    [1, 2, 3]
    >>> smallest_to_largest([9, 6, 3])
    [3, 6, 9]
    >>> smallest_to_largest([1, 1, 0])
    [0, 1, 1]
    """
    pass  # TODO: Implement this function


def median_element(array):
    """
    Returns the median value of the elements in the array.

    Examples:
    >>> median_element([2, 3, 1])
    2
    >>> median_element([9, 6, 3])
    6
    >>> median_element([1, 1, 0])
    1
    """
    pass  # TODO: Implement this function


def mode_element(array):
    """
    Returns the mode value of the elements in the array.

    Examples:
    >>> mode_element([1, 1, 0, 2, 1])
    1
    >>> mode_element([2, 3, 0, 2, 1])
    2
    >>> mode_element([3, 5, 0, 2, 3])
    3
    """
    pass  # TODO: Implement this function


def reverse_elements(array):
    """
    Returns the array with the order of its elements reversed.

    Examples:
    >>> reverse_elements([3, 1, 0, 2, 1])
    [1, 2, 0, 1, 3]
    >>> reverse_elements([2, 3, 0, 2, 5])
    [5, 2, 0, 3, 2]
    >>> reverse_elements([3, 5, 0, 2, 3])
    [3, 2, 0, 5, 3]
    """
    pass  # TODO: Implement this function

def remove_duplicates(array):
    """
    Returns the array with all the duplicate values removed.

    Examples:
    >>> remove_duplicates([3, 1, 0, 2, 1])
    [3, 1, 0, 2]
    >>> remove_duplicates([2, 3, 0, 2, 5])
    [2, 3, 0, 5]
    >>> remove_duplicates([3, 5, 3, 3, 3])
    [3, 5]
    """
    pass  # TODO: Implement this function

# task 1

num = 43197

def sum_of_numbers(number: int) -> int:
    """
    Recursively calculates the sum of all digits of an integer.
    :param number: non-negative integer
    :return: the sum of all digits in given number
    """
    if number == 0:
        return 0
    return number % 10 + sum_of_numbers(number // 10)

print(sum_of_numbers(num))


# task 2

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

def sum_of_nested_numbers(numbers: list) -> int:
    """
    The function takes list of integers and lists with integers of any depth,
    recursively sums all integers and returns final number.
    :param numbers: list of integers and/or sublists with integers.
    :return: int, the sum of all integers in the list and its sublists.
    """
    if not numbers:
        return 0
    first, last = numbers[0], numbers[1:]
    if isinstance(first, list):
        return sum_of_nested_numbers(first) + sum_of_nested_numbers(last)
    else:
        return first + sum_of_nested_numbers(last)

print(sum_of_nested_numbers(nested_numbers))


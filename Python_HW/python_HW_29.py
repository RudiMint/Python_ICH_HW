# task 1

def fibonacci_generator(number1, number2):
    r"""
    Generate an infinite Fibonacci-like sequence.

    This generator continuously yields the sum of the two previous
    numbers, updating the sequence after each iteration.

    Args:
        number1 (int | float): The first starting number.
        number2 (int | float): The second starting number.

    Yields:
        int | float: The next value in the sequence.
    """
    while True:
        value = number1 + number2
        yield value
        number1 = number2
        number2 = value

gen = fibonacci_generator(0, 1)

for _ in range(10):
    print(next(gen))

print("new task >>>>")
# task 2

data_list = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

def unique_gen(data):
    """
    Yield unique items from an iterable while preserving order.
    This generator iterates through the input data and yields each
    value only the first time it appears.
    Args:
        data (iterable): Input sequence or iterable containing values.
    Yields:
        Any: Unique values from the input iterable in their original order.
    """
    seen = set()
    for value in data:
        if value not in seen:
            seen.add(value)
            yield value

gen2 = unique_gen(data_list)

for e in gen2:
    print(e)

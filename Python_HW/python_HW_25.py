import logging


logging.basicConfig(
    filename="error.log",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
    level=logging.ERROR
)


def divide(first, second):
    """
    Divide two numbers and return the result.
    Args:
        first (int | float): The numerator.
        second (int | float): The denominator.
    Returns:
        float: Result of dividing first by second.
    """
    result = first / second
    return result

while True:
    try:
        first1 = int(input("enter first number >>> "))
        second2 = int(input("enter second number >>> "))

        print(divide(first1, second2))
        break

    except ValueError as e:
        logging.error(f"Invalid input: {e}")
        print("Please enter valid integers")

    except ZeroDivisionError as e:
        logging.error(f"Math error: {e}")
        print("Cannot divide by zero")

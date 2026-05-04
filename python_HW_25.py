import logging


logging.basicConfig(
    filename="error.log",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
    level=logging.ERROR
)

def divide():
    """
        Prompts the user to enter two numbers (dividend and divisor),
        performs division, and handles possible errors.

        Handled exceptions:
        - ValueError: if the input is not a valid number
        - ZeroDivisionError: if attempting to divide by zero

        The function keeps asking for input until valid data is provided.
        After a successful division, it prints the result.
    """
    while True:
        try:
            first = int(input("enter first number >>> "))
            second = int(input("enter second number >>> "))
            result = first / second
            return result
        except (ValueError, ZeroDivisionError) as e:
            print(f"exception: {e}")
            logging.error(f"exception: {e}")

print(divide())


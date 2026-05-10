from datetime import datetime


# task 1

def make_rounder(digits):
    """
    Create and return a rounding function with a fixed number of decimal places.
    Args:
        digits (int): The number of decimal places to round to.
    Returns:
        function: A function that takes a number and returns it rounded
        to the specified number of decimal places.
    """
    def round_number(number):
        """
        Round a number to the predefined number of decimal places.
        Args:
            number (float): The number to round.
        Returns:
            float: The rounded number.
        """
        return round(number, digits)
    return round_number

round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))


# task 2

def create_logger():
    """
    Creates a simple closure-based logger.
    The logger stores messages with timestamps in an internal list
    that persists across function calls.
    Returns:
        function: A logger function that accepts an optional message.
    Logger behavior:
        - If called with a message (string), it appends:
              "message: YYYY-MM-DD HH:MM:SS"
          to the internal event list.
        - If called without arguments, it returns the full list
          of logged events.
    """
    events = []

    def loger(message=None):
        if message is not None:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"{message}: {current_time}")
        return events
    return loger


log = create_logger()

log("Loading data")
log("Processing completed")
log("File saved")

for event in log():
    print(event)


# task 3

def frame(func):
    """
    Decorator that visually frames the output of a function call
    using separator lines.
    It prints a line of dashes before and after the wrapped function
    execution, making console output easier to read.
    Args:
        func (callable): The function to be wrapped.
    Returns:
        callable: The wrapped function that prints framing lines
        around the original function's output.
    """
    def wrapper(*args, **kwargs):
        print("-" * 50)
        result = func(*args, **kwargs)
        print("-" * 50)
        return result
    return wrapper

@frame
def say_hello():
    print("Hello, player!")


say_hello()

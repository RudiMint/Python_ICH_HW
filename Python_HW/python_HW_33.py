import time

from functools import wraps


def measure_time(repeats):
    """
    Decorator factory for measuring average execution time.
    Args:
        repeats (int): Number of times the function should be executed.
    Returns:
        function: Decorated function with timing measurement.
    """
    def decorator(func):
        """
        Decorates a function and measures its average runtime.
        Args:
            func (function): Function to decorate.
        Returns:
            function: Wrapped function.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Executes the function multiple times and
            prints the average execution time.
            Args:
                *args: Positional arguments for the function.
                **kwargs: Keyword arguments for the function.
            Returns:
                Any: Result of the last function execution.
            """
            times = []

            for i in range(repeats):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                times.append(end_time - start_time)

            avg_time = sum(times) / len(times)

            print(f"average processing time in {repeats} calls: {avg_time:.6f} sec")

            return result

        return wrapper
    return decorator

@measure_time(10)
def compute():
    """
    Calculates the sum of numbers from 0 to 9,999,999.
    Returns:
        int: Computed sum.
    """
    total = 0

    for i in range(10_000_000):
        total += i

    return total


print(f"result: {compute()}")

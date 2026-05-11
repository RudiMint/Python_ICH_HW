import time

from functools import wraps


def measure_time(repeats):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
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
    total = 0

    for i in range(10_000_000):
        total += i

    return total


print(f"result: {compute()}")

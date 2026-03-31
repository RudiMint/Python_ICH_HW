# task 1

n = 17

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if is_prime(n):
    print(f"number {n} is prime")
else:
    print(f"number {n} is not prime")


# task 2

def filter_numbers(filter_type, *args):
    if filter_type == "even":
        return [num for num in args if num % 2 == 0]
    elif filter_type == "odd":
        return [num for num in args if num % 2 != 0]
    elif filter_type == "prime":
        return [num for num in args if is_prime(num)]
    else:
        return "invalid filter"


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))

print(filter_numbers("odd", 10, 15, 20, 25))

print(filter_numbers("prime", 2, 3, 5, 7))

print(filter_numbers("primes", 2, 3, 5, 7))


# task 3

dict1 = {"a": 1, "b": 2}

dict2 = {"b": 3, "c": 4}

dict3 = {"d": 5}

def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

print(merge_dicts(dict1, dict2, dict3))


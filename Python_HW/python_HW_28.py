import itertools
# task 1

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

# def day_generator(schedule):
#     while True:
#         for day, tasks in schedule.items():
#             yield day, tasks
#
# generator = day_generator(weekly_schedule)
#
# days_cycle = itertools.cycle(weekly_schedule.items())
#
# while True:
#     input("press 'Enter' to get the plan")
#
#     # day, tasks = next(generator)
#     day, tasks = next(days_cycle)
#     print(f"\n{day}: {', '.join(tasks)}\n")


# task 2

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

# def combined_list(a, b, *args):
#     merged_list = itertools.chain(a,b, *args)
#     while True:
#         try:
#             groceries = next(merged_list)
#             print(f"{groceries}\n")
#         except StopIteration:
#             break

def combined_list(a, b, *args):
    """
    Combines multiple iterables into a single sequence using itertools.chain
    and prints each element in a clean, Pythonic way.

    This is the recommended approach because it is:
    - More readable
    - Less error-prone
    - Idiomatic Python

    Args:
        a (iterable): First list of items.
        b (iterable): Second list of items.
        *args (iterables): Additional lists of items.

    Returns:
        None
    """
    for item in itertools.chain(a, b, *args):
        print(f"{item}\n")

combined_list(fruits, vegetables, dairy)


# task 3

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

def mixing_clothes(a, b, *args):
    """
    Generates and prints all possible combinations (Cartesian product)
    of multiple iterables using itertools.product.

    Each combination represents one possible outfit configuration
    based on clothing items, colors, and sizes.

    Args:
        a (iterable): First iterable (e.g., clothing items).
        b (iterable): Second iterable (e.g., colors).
        *args (iterables): Additional iterables (e.g., sizes, styles, etc.).

    Behavior:
        - Computes the Cartesian product of all input iterables.
        - Joins each resulting tuple into a string separated by " - ".
        - Prints each combination on a new line.

    Returns:
        None
    """
    for item in itertools.product(a, b, *args):
        print(f"{' - '.join(item)}\n")

mixing_clothes(clothes, colors, sizes)

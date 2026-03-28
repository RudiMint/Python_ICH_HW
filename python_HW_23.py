from typing import Any


data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

def concatenation(data_list: list[Any]) -> str:
    """
    The function takes list of any data and
    returns all the elements of the list
    concatenated into a string separated by " | ".
    :param data_list: list
    :return: string
    """
    return " | ".join(str(x) for x in data_list)

print(concatenation(data))


# task 2

data1 = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

# def total_scores(data_list: list[dict]) -> int:
#     """
#     Sum all integers from the "scores" lists in each dictionary.
#     :param data_list: list of dictionaries containing a "scores" key.
#     :return: total sum of all scores.
#     """
#     return sum(map(lambda x: sum(x["scores"]), data_list))
#
# print(f"total score >>> {total_scores(data1)}")

def total_scores(data_list: list[dict[str, list[int]]]) -> int:
    """
    Sum all integers from the "scores" lists in each dictionary.
    :param data_list: list of dictionaries containing a "scores" key.
    :return: total sum of all scores.
    """
    return sum(sum(item["scores"]) for item in data_list)

print(f"total score >>> {total_scores(data1)}")


# task 1

def matched_lines_search(file_name, key_word):
    """
    Searches for lines containing a given keyword in a text file and saves them to a new file.

    Parameters:
        file_name (str): The name (or path) of the file to search in.
        key_word (str): The keyword to search for within the file.

    Behavior:
        - Reads all lines from the specified file.
        - Performs a case-insensitive search for the keyword in each line.
        - If matching lines are found:
            - Creates a new file named "<keyword>_<original_file_name>".
            - Writes all matching lines into the new file.
            - Prints a success message.
        - If no matches are found:
            - Prints a message indicating no matches.
        - If the file does not exist:
            - Catches FileNotFoundError and prints an error message.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        matched_lines = [line for line in lines if key_word.lower() in line.lower()]

        if matched_lines:
            new_file_name = f"{key_word}_{file_name}"
            with open(new_file_name, "w", encoding="utf-8") as new_file:
                new_file.writelines(matched_lines)
            print(f"lines containing {key_word} have been saved to {new_file_name}")
        else:
            print(f"lines containing {key_word} are not found")
    except FileNotFoundError:
        print("File not found")

# file name "system_log.txt"
# key word "error"
file_name1 = input("enter file name to search >>> ")
key_word1 = input("enter key word >>> ")

matched_lines_search(file_name1, key_word1)


# task 2

def remove_duplicates(file_name):
    """
    Remove duplicate lines from a text file and save the unique lines to a new file.

    This function reads all lines from the specified file, removes duplicates
    while preserving the original order, and writes the unique lines to a new
    file prefixed with 'unique_'.

    Parameters:
        file_name (str): The path to the input file containing lines of text.

    Output:
        Creates a new file named 'unique_<file_name>' containing only unique lines.

    Exceptions:
        Prints an error message if the file is not found.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        seen = set()
        unique_lines = []

        for line in lines:
            if line not in seen:
                unique_lines.append(line)
                seen.add(line)

        new_file_name = f"unique_{file_name}"

        with open(new_file_name, "w") as new_file:
            new_file.writelines(unique_lines)

        print(f"Duplicates have been removed. Unique rows have been saved to {new_file_name}")

    except FileNotFoundError:
        print("File not found")

# file name 2 = "movies_to_watch.txt"
file_name2 = input("enter file name to extract unique rows >>>")

remove_duplicates(file_name2)


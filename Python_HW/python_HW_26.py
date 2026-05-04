import os
import sys
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


logger = logging.getLogger(__name__)


# task 1

def list_directory_contents(path):
    r"""
    List contents of a directory.

    Separates and logs folders and files found in the given path.

    Args:
        path (str): Path to the directory.

    Raises:
        Logs errors if:
            - Directory does not exist
            - Path is not a directory
            - Permission is denied

    Usage:
        script.py <path>

    Example:
        python script.py C:/Users/Example
    """
    try:
        folders = []
        files = []

        for item in os.listdir(path):
            fullpath = os.path.join(path, item)
            if os.path.isdir(fullpath):
                folders.append(item)
            elif os.path.isfile(fullpath):
                files.append(item)

        logger.info(f"contents of directory '{path}':\n")

        logger.info("Folders:")
        for folder in folders:
            logger.info(f"- {folder}")

        logger.info("\nFiles:")
        for filename in files:
            logger.info(f"- {filename}")

    except (FileNotFoundError, NotADirectoryError, PermissionError) as er:
        logger.error(f"exception: {er}")


# task 2

def find_files(root_dir, extension):
    """
    Recursively search for files with a given extension.

    Args:
        root_dir (str): Root directory to start search from.
        extension (str): File extension to search for (without dot).

    Returns:
        list: List of full file paths matching the extension.

    Notes:
        - Uses os.walk to traverse directories.
        - Logs each found file.
    """
    found_files = []

    try:
        for dir_path, dir_names, file_names in os.walk(root_dir):
            for file_name in file_names:
                if file_name.endswith(extension):
                    full_path = os.path.join(dir_path, file_name)
                    found_files.append(full_path)
                    logger.info(f"file found: {full_path}")
    except Exception as e:
        logger.error(f"error while searching for files: {e}")

    return found_files


def deleting_files(files):
    """
    Delete a list of files.

    Args:
        files (list): List of file paths to delete.

    Notes:
        - Logs each deletion.
        - Logs error if file is not found.
    """
    for file_path in files:
        try:
            os.remove(file_path)
            logger.info(f"file removed: {file_path}")
        except FileNotFoundError as e:
            logger.error(f"error: {e}")



def main():
    r"""
        Entry point of the script.

        Behavior:
            - If 1 argument is provided:
                Lists directory contents.
            - If 2 arguments are provided:
                Searches for files with a given extension and optionally deletes them.

        Command-line usage:
            python script.py <directory>
            python script.py <directory> <extension>

        Examples:
            python script.py C:/Users/Example
            python script.py C:/Users/Example txt
        """

    if len(sys.argv) == 2:
        list_directory_contents(sys.argv[1])

    elif len(sys.argv) == 3:

        root_dir = sys.argv[1]
        extension = sys.argv[2]
        extension = extension.lower().lstrip('.')

        if not os.path.isdir(root_dir):
            logger.info("directory not found")
            return

        files = find_files(root_dir, extension)

        if not files:
            logger.info(f"files with extension '{extension}' not found")
            return

        logger.info(f"\nfiles with extension '{extension}':\n")
        for f in files:
            logger.info(f"- {f}")

        answer = input("\ndelete chosen files? (y/n): ").strip().lower()

        if answer == 'y':
            deleting_files(files)
            logger.info("deleted successfully.")
        else:
            logger.info("deletion canceled.")


main()

from pathlib import Path
import re

invalid_characters = r'[<>:"\|*?]'

def create_directory(path: str):
    """
    Creates a directory with the given name, located inside the given parent directory.

    Returns an error if the specified directory name is empty.
    Returns an error if the specified directory name is illegal.
    Returns an error if the specified parent directory does not exist.

    Arguments:
    Path: a string representation of the desired path to be created. 
    Returns:
    Path object to the newly created directory.
    """
    # validating arguments passed in
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    if path == "":
        raise ValueError("Path of directory cannot be empty")
    if re.search(invalid_characters, path):
        raise ValueError("Directory name contains at least one illegal character")

    return None
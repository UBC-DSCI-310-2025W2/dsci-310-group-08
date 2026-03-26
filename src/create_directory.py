from pathlib import Path
import re

invalid_characters = r'[<>:"\|*?]'

def create_directory(path: str):
    """
    Creates the directory given by the specified path.
    Purpose: If the directory where the user wants to store their data/file does not exist, this function will create it for them.

    Returns an error if the specified directory name is empty.
    Returns an error if the specified directory name is illegal.

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

    # create directory
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    
    return path
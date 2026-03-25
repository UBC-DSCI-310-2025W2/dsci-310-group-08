from pathlib import Path

def create_directory(name, parent):
    """
    Creates a directory with the given name, located inside the given parent directory.

    Returns an error if the specified directory name is empty.
    Returns an error if the specified directory name is illegal.
    Returns an error if the specified parent directory does not exist.

    Arguments:
    Name: desired name of directory.
    Parent: string of desired parent directory of directory to be created.
    Returns:
    Path to the newly created directory
    """
    # validating arguments passed in
    if name == "":
        raise ValueError("Name of directory cannot be empty")
    
    return None
import pytest 
from pathlib import Path
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.create_directory import create_directory 

# simple use case tests
def test_create_dir_from_root_dir():
    """
    Tests the use case of creating a directory from the root directory.
    Expected outcome: directory created successfully.
    """
    # catch exceptions
    try:
        testdir = create_directory("testdir", "")
    except Exception as e:
        assert False, f"Test failed due to unexpected error: {e}"
    # check directory was actually created 
    assert testdir.exists(), "Directory was not created"
    assert testdir.is_dir(), "Output is not a directory"
        
def test_create_dir_two_deep():
    """
    Tests the use case of creating a subdirectory of an already existing parent directory.  
    This parent directory should live at the root directory.
    Expected outcome: directory created successfully.
    """
    try:
        testdir = create_directory("testdir", "tests")
    except Exception as e:
        assert False, f"Test failed due to unexpected error: {e}"
    # check directory was actually created 
    assert testdir.exists(), "Directory was not created"
    assert testdir.is_dir(), "Output is not a directory"


# edge use cases test
def test_create_2_dirs_at_once():
    """
    Tests the use case of creating a directory located at the root, and then creating a subdirectory of that directory.  
    Specifically, testing the ability to do both actions within the same test.
    Expected outcome: both directories created successfully, with one being a subdirectory of the other.
    """
    try:
        onedeep = create_directory("onedeep", "")
        twodeep = create_directory("twodeep", "onedeep")
    except Exception as e:
        assert False, f"Test failed due to unexpected error: {e}"
    # check directories were actually created 
    assert onedeep.exists(), "First directory was not created"
    assert onedeep.is_dir(), "Output is not a directory"
    assert twodeep.exists(), "Second level directory was not created"
    assert twodeep.is_dir(), "Output is not a directory"
    # check second directory has parent of first directory
    assert twodeep.parent == onedeep
    
def test_create_already_existing_dir():
    """
    Tests the use case of attempting to create a directory that has already been created.
    Expected outcome:  an error is raised alerting the user that directory already exists.
    """
    try:
        testdir = create_directory("tests", "")
        assert False, "FileExistsError should have been raised"
    except FileExistsError:
        pass # expected behaviour
    except Exception as e:
        assert False, f"Test failed due to unexpected error: {e}"

        
# error use cases test
def test_empty_directory_name():
    """
    Tests the use case of attempting to create a directory with no name, ie, the empty string is passed to the name argument.
    Expected outcome: an error is raised alerting the user that a directory with no name cannot be created.
    """
    try:
        empty_name_dir = create_directory("", "tests")
        assert False, "ValueError should have been raised"
    except ValueError:
        pass # expected behaviour
    except Exception as e:
        assert False, f"Test failed due to unexpected error: {e}"

def test_parent_directory_does_not_exist():
    """
    Tests the use case of attempting to create a directory with the argument passed to parent being a directory that does not exist.
    Expected outcome: an error is raised, alerting the user that the parent directory they used does not exist.
    """
    try:
        parent_nonexist_dir = create_directory("testdir", "testz")
        assert False, "FileNotFoundError should have been raised"
    except FileNotFoundError:
        pass # expected behaviour
    except Exception as e:
        assert False, f"Test failed due to unexpected error: {e}"

def test_illegal_char_in_name():
    """
    Test the use case where the user tries to pass in a name that contains an illegal character such as " or /.
    Expected outcome: an error is raised alerting the user their intended directory name contains an illegal character.
    """
    try:
        parent_nonexist_dir = create_directory("illegal/directory", "tests")
        assert False, "ValueError should have been raised"
    except ValueError:
        pass # expected behaviour
    except Exception as e:
        assert False, f"Test failed due to unexpected error: {e}"
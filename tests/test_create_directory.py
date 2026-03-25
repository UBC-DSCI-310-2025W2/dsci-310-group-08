import pytest 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.create_directory import create_directory 

# simple use case tests
def test_create_dir_from_root_dir():
    """
    Tests the use case of creating a directory from the root directory.
    Expected outcome:  directory created successfully.
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
    Expected outcome:  directory created successfully.
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
    Expected outcome:  both directories created successfully, with one being a subdirectory of the other.
    """
    assert False, "test not implemented yet"

def test_create_already_existing_dir():
    """
    Tests the use case of attempting to create a directory that has already been created.
    Expected outcome:  an error is raised alerting the user that directory already exists.
    """
    assert False, "test not implemented yet"



# error use cases test
import pytest 

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

# edge use case test

# error use cases test
import pytest 
import pandas as pd
import sys
import os

# Import the find_measurement_last_time function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.find_measurement_last_time import find_measurement_last_time

##============
## Setup data
##============

# Input test data

## Expected case data 1
two_groups_3_consecutive_years_mixed_order = pd.DataFrame({'year': [2019,2020,2018,2020,2018,2019],
                                                           'city': ["Vic","Van","Van","Vic","Vic","Van"],
                                                           'rank': [1,9,15,3,4,5]})

## Expected case data 2
three_groups_diff_consecutive_years_mixed_order = pd.DataFrame({'year': [2020,2019,2018,2017,2011,2010,2020],
                                                                'city': ["NYC","Van","Van","Van","Vic","Vic","Van"],
                                                                'rank': [1,9,15,3,4,5,99]})

## Edge case data
one_group_non_consecutive_years_non_numerical_measurement = pd.DataFrame({'year': [2025, 2020, 2015, 2010],
                                                                          'city': ["Van","Van","Van","Van"],
                                                                          'grades': ["A","B","A+","A-"]})

## Error case data
missing_measurement_data = pd.DataFrame({'year': [2025, 2020, 2015, 2010],
                                         'city': ["Van","Van","Van","Van"],
                                         'rank': [1,9,None,3]})

# Expected output data

## Expected case 1
output_expected_1 = pd.DataFrame({'year': [2018, 2019, 2020, 2018, 2019, 2020],
                                  'city': ["Van","Van","Van","Vic","Vic","Vic"],
                                  'rank': [15, 5, 9, 4, 1, 3],
                                  'rank_last_time': [15.0, 15.0, 5.0, 4.0, 4.0, 1.0]})

## Expected case 2
output_expected_2 = pd.DataFrame({'year': [2020, 2017, 2018, 2019, 2020, 2010, 2011],
                                  'city': ["NYC","Van","Van","Van","Van","Vic","Vic"],
                                  'rank': [1, 3, 15, 9, 99, 5, 4],
                                  'rank_last_time': [1.0, 3.0, 3.0, 15.0, 9.0, 5.0, 5.0]})

## Edge case
output_edge = pd.DataFrame({'year': [2010, 2015, 2020, 2025],
                            'city': ["Van","Van","Van","Van"],
                            'grades': ["A-","A+","B","A"],
                            'grades_last_time': ["A-", "A-", "A+", "B"]})

##============
## Tests
##============

## Expected case 1
def test_two_groups_3_consecutive_years_mixed_order():
    """
    Tests the expected case which we have two cities and numerical measurements from three 
    consecutive years with mixed orders.
    """
    data_frame_processed = find_measurement_last_time(two_groups_3_consecutive_years_mixed_order,
                                                      'year', 'city', 'rank')
    
    # pandas testing utility for comparing DataFrames
    pd.testing.assert_frame_equal(data_frame_processed.reset_index(drop=True), 
                                  output_expected_1.reset_index(drop=True))

## Expected case 2
def test_three_groups_diff_consecutive_years_mixed_order():
    """
    Tests the expected case which we have three cities and numerical measurements from different 
    consecutive years with mixed orders.
    """
    data_frame_processed = find_measurement_last_time(three_groups_diff_consecutive_years_mixed_order,
                                                      'year', 'city', 'rank')
    
    # pandas testing utility for comparing DataFrames
    pd.testing.assert_frame_equal(data_frame_processed.reset_index(drop=True), 
                                  output_expected_2.reset_index(drop=True))

## Edge case 
def test_one_group_non_consecutive_years_non_numerical_measurement():
    """
    Tests the edge case which we have only one city and non-numerical measurements 
    from non-consecutive years.
    """
    data_frame_processed = find_measurement_last_time(one_group_non_consecutive_years_non_numerical_measurement,
                                                      'year', 'city', 'grades')
    
    # pandas testing utility for comparing DataFrames
    pd.testing.assert_frame_equal(data_frame_processed.reset_index(drop=True), 
                                  output_edge.reset_index(drop=True))
    
## Error case
def test_missing_measurement_data():
    """
    Tests the error case which the measurement column has some missing data.
    We expect the function will raise a ValueError.
    """

    # We expect a ValueError to be raised here
    with pytest.raises(ValueError, 
                       match="The measurement column should not have any missing values."):
        find_measurement_last_time(missing_measurement_data, 'year', 'city', 'rank')



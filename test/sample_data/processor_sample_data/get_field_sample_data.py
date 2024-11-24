"""
This module contains sample data for testing the get_field method of the DataProcessor class.
"""

get_field_sample_data = {
    "field_exists": {
        "sample_data": {"record": {"field1": "value1", "field2": "value2"}, "field_name": "field1"},
        "expected_result": "value1",
    },
    "field_missing": {
        "sample_data": {"record": {"field1": "value1", "field2": "value2"}, "field_name": "field3"},
        "expected_result": None,
    },
    "empty_record": {
        "sample_data": {"record": {}, "field_name": "field1"},
        "expected_result": None,
    },
    "nested_field": {
        "sample_data": {"record": {"field1": {"subfield1": "subvalue1"}}, "field_name": "field1"},
        "expected_result": {"subfield1": "subvalue1"},
    },
}

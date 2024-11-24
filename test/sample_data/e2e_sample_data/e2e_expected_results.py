"""
This module contains the expected results for the end-to-end tests of the DataProcessor class.
"""

e2e_expected_results = {
    "with_errors": {
        "missing": {
            "0B31D33076B73E35F140F4701F69168C": [1, 2, 3, 4, 24],
            "E4086102EB4BAFB97DF4765B69B1DB9A": [19, 27],
            "CECFA0D206F9A331099A7C65765A3FBD": [2],
        },
        "identical_duplicates": {
            "0B31D33076B73E35F140F4701F69168C": {11: 5},
        },
        "different_duplicates": {
            "0B31D33076B73E35F140F4701F69168C": {11: 1},
        },
        "indexing_errors": {
            "0B31D33076B73E35F140F4701F69168C": {
                "invalid_type": [
                    "Expected: int, Found: str for index: kjasd",
                    "Expected: int, Found: str for index: string",
                ],
                "out_of_range": [333, -2, 0],
            },
            "E4086102EB4BAFB97DF4765B69B1DB9A": {
                "out_of_range": [12229, 28],
            },
        },
        "invalid_document_counts": {},
        "distinct_stories_count": 273,
    },
    "without_errors": {
        "missing": {},
        "identical_duplicates": {},
        "different_duplicates": {},
        "indexing_errors": {},
        "invalid_document_counts": {},
        "distinct_stories_count": 273,
    },
}

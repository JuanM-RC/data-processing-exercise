"""
This module contains sample data for testing the format_process_data_logs function.
"""

format_process_data_logs_sample_data = {
    "no_errors": {
        "results": {
            "distinct_stories_count": 5,
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {},
        },
        "expected_result": "Number of distinct stories: 5",
    },
    "missing_indices": {
        "results": {
            "distinct_stories_count": 5,
            "missing": {
                "DOC123": [1, 2, 3],
            },
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {},
        },
        "expected_result": (
            "Number of distinct stories: 5\n"
            "\nDocument ID DOC123:\n"
            "    - Missing indices: [1, 2, 3]"
        ),
    },
    "identical_duplicates": {
        "results": {
            "distinct_stories_count": 5,
            "missing": {},
            "identical_duplicates": {
                "DOC123": {1: 2, 2: 1},
            },
            "different_duplicates": {},
            "indexing_errors": {},
        },
        "expected_result": (
            "Number of distinct stories: 5\n"
            "\nDocument ID DOC123:\n"
            "    - Identical duplicate indices: index: 1, repeated: 2 times, index: 2, repeated: 1 time"
        ),
    },
    "different_duplicates": {
        "results": {
            "distinct_stories_count": 5,
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {
                "DOC123": {1: 2, 2: 1},
            },
            "indexing_errors": {},
        },
        "expected_result": (
            "Number of distinct stories: 5\n"
            "\nDocument ID DOC123:\n"
            "    - Different duplicate indices: index: 1, repeated: 2 times, index: 2, repeated: 1 time"
        ),
    },
    "indexing_errors_invalid_type": {
        "results": {
            "distinct_stories_count": 5,
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {
                "DOC123": {
                    "invalid_type": ["Type error 1", "Type error 2"],
                },
            },
        },
        "expected_result": (
            "Number of distinct stories: 5\n"
            "\nDocument ID DOC123:\n"
            "    - Invalid Type Errors:\n        Type error 1\n        Type error 2"
        ),
    },
    "indexing_errors_out_of_range": {
        "results": {
            "distinct_stories_count": 5,
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {
                "DOC123": {
                    "out_of_range": [5, 3, 1],
                },
            },
        },
        "expected_result": (
            "Number of distinct stories: 5\n"
            "\nDocument ID DOC123:\n"
            "    - Out of Range Errors:\n        Out of range index: 1\n        Out of range index: 3\n        Out of range index: 5"
        ),
    },
    "combined_errors": {
        "results": {
            "distinct_stories_count": 5,
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {
                "DOC123": {
                    "invalid_type": ["Type error 1"],
                    "out_of_range": [2, 4],
                },
            },
        },
        "expected_result": (
            "Number of distinct stories: 5\n"
            "\nDocument ID DOC123:\n"
            "    - Invalid Type Errors:\n        Type error 1\n"
            "    - Out of Range Errors:\n        Out of range index: 2\n        Out of range index: 4"
        ),
    },
}

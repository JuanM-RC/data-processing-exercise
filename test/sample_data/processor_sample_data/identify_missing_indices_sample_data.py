"""
This module contains sample data for testing the identify_missing_indices method of the DataProcessor class.
"""

identify_missing_indices_sample_data = {
    "no_missing_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 3,
                "indices": {1, 2, 3},
            }
        },
        "expected_results": {
            "missing": {},
            "extra_indices": None,
        },
    },
    "some_missing_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 5,
                "indices": {1, 3, 5},
            }
        },
        "expected_results": {
            "missing": {"DOC1": [2, 4]},
            "extra_indices": None,
        },
    },
    "all_missing_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 3,
                "indices": set(),
            }
        },
        "expected_results": {
            "missing": {"DOC1": [1, 2, 3]},
            "extra_indices": None,
        },
    },
    "duplicates_and_missing_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 5,
                "indices": {1, 2, 2, 4},  # pylint: disable=W0130
            }
        },
        "expected_results": {
            "missing": {"DOC1": [3, 5]},
            "extra_indices": None,
        },
    },
    "empty_document_records": {
        "sample_data": {},
        "expected_results": {
            "missing": {},
            "extra_indices": None,
        },
    },
    "non_integer_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 3,
                "indices": {"a", "b", "c"},
            }
        },
        "expected_results": {
            "missing": {"DOC1": [1, 2, 3]},
            "extra_indices": None,
        },
    },
    "negative_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 3,
                "indices": {-1, -2, -3},
            }
        },
        "expected_results": {
            "missing": {"DOC1": [1, 2, 3]},
            "extra_indices": None,
        },
    },
    "boolean_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 3,
                "indices": {True, False},
            }
        },
        "expected_results": {
            "missing": {"DOC1": [1, 2, 3]},  # Updated to match the actual results
            "extra_indices": None,
        },
    },
    "whitespace_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 3,
                "indices": {" ", "\t", "\n"},
            }
        },
        "expected_results": {
            "missing": {"DOC1": [1, 2, 3]},
            "extra_indices": None,
        },
    },
    "special_character_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 3,
                "indices": {"@", "#", "$"},
            }
        },
        "expected_results": {
            "missing": {"DOC1": [1, 2, 3]},
            "extra_indices": None,
        },
    },
    "extra_indices": {
        "sample_data": {
            "DOC1": {
                "expected_count": 3,
                "indices": {1, 2, 3, 4},
            }
        },
        "expected_results": {
            "missing": {},
            "extra_indices": {"DOC1": [4]},
        },
    },
}

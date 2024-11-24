"""
This module contains sample data for testing the process_analytics method of the DataProcessor class.
"""

process_analytics_sample_data = {
    "no_records": {
        "sample_data": [],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {},
            "invalid_document_counts": {},
            "distinct_stories_count": 0,
        },
    },
    "single_record": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 1}
        ],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {},
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "multiple_records": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 2},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 2, "DOCUMENT_RECORD_COUNT": 2},
            {"RP_DOCUMENT_ID": "DOC2", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 1},
        ],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {},
            "invalid_document_counts": {},
            "distinct_stories_count": 2,
        },
    },
    "missing_indices": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 3},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 3, "DOCUMENT_RECORD_COUNT": 3},
        ],
        "expected_results": {
            "missing": {"DOC1": [2]},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {},
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "duplicates": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 2},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 2},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 2, "DOCUMENT_RECORD_COUNT": 2},
        ],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {"DOC1": {1: 1}},
            "different_duplicates": {},
            "indexing_errors": {},
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "invalid_document_ids": {
        "sample_data": [
            {"RP_DOCUMENT_ID": None, "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 1},
            {"RP_DOCUMENT_ID": "", "DOCUMENT_RECORD_INDEX": 2, "DOCUMENT_RECORD_COUNT": 1},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 1},
        ],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {
                "invalid_document_ids": [
                    {
                        "RP_DOCUMENT_ID": None,
                        "RP_ENTITY_ID": None,
                        "record": {
                            "RP_DOCUMENT_ID": None,
                            "DOCUMENT_RECORD_INDEX": 1,
                            "DOCUMENT_RECORD_COUNT": 1,
                        },
                    },
                    {
                        "RP_DOCUMENT_ID": "",
                        "RP_ENTITY_ID": None,
                        "record": {
                            "RP_DOCUMENT_ID": "",
                            "DOCUMENT_RECORD_INDEX": 2,
                            "DOCUMENT_RECORD_COUNT": 1,
                        },
                    },
                ]
            },
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "invalid_indices": {
        "sample_data": [
            {
                "RP_DOCUMENT_ID": "DOC1",
                "DOCUMENT_RECORD_INDEX": "invalid",
                "DOCUMENT_RECORD_COUNT": 1,
            },
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 2, "DOCUMENT_RECORD_COUNT": 1},
        ],
        "expected_results": {
            "missing": {"DOC1": [1]},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {
                "DOC1": {
                    "invalid_type": ["Expected: int, Found: str for index: invalid"],
                    "out_of_range": [2],
                }
            },
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "boolean_values": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": True, "DOCUMENT_RECORD_COUNT": 1},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 2, "DOCUMENT_RECORD_COUNT": 1},
        ],
        "expected_results": {
            "missing": {"DOC1": [1]},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {
                "DOC1": {
                    "invalid_type": ["Expected: int, Found: bool for index: True"],
                    "out_of_range": [2],
                }
            },
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "empty_string_document_id": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 1},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 2, "DOCUMENT_RECORD_COUNT": 1},
        ],
        "expected_results": {
            "missing": {"DOC1": [1]},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {
                "invalid_document_ids": [
                    {
                        "RP_DOCUMENT_ID": "",
                        "RP_ENTITY_ID": None,
                        "record": {
                            "RP_DOCUMENT_ID": "",
                            "DOCUMENT_RECORD_INDEX": 1,
                            "DOCUMENT_RECORD_COUNT": 1,
                        },
                    }
                ],
                "DOC1": {"out_of_range": [2]},
            },
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "whitespace_string_document_id": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "   ", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 1},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 2, "DOCUMENT_RECORD_COUNT": 1},
        ],
        "expected_results": {
            "missing": {"DOC1": [1]},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {
                "DOC1": {"out_of_range": [2]},
                "invalid_document_ids": [
                    {
                        "RP_DOCUMENT_ID": "   ",
                        "RP_ENTITY_ID": None,
                        "record": {
                            "RP_DOCUMENT_ID": "   ",
                            "DOCUMENT_RECORD_INDEX": 1,
                            "DOCUMENT_RECORD_COUNT": 1,
                        },
                    }
                ],
            },
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "special_characters_entity_ids": {
        "sample_data": [
            {
                "RP_DOCUMENT_ID": "DOC1",
                "DOCUMENT_RECORD_INDEX": 1,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": "@#$%",
            },
            {
                "RP_DOCUMENT_ID": "DOC1",
                "DOCUMENT_RECORD_INDEX": 2,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": "ENTTY1",
            },
        ],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {"DOC1": {"out_of_range": [2]}},
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "boolean_values_entity_ids": {
        "sample_data": [
            {
                "RP_DOCUMENT_ID": "DOC1",
                "DOCUMENT_RECORD_INDEX": 1,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": True,
            },
            {
                "RP_DOCUMENT_ID": "DOC1",
                "DOCUMENT_RECORD_INDEX": 2,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": "ENTTY1",
            },
        ],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {"DOC1": {"out_of_range": [2]}},
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "nested_data_structures": {
        "sample_data": [
            {
                "RP_DOCUMENT_ID": "DOC1",
                "DOCUMENT_RECORD_INDEX": 1,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": {"nested": "value"},
            },
            {
                "RP_DOCUMENT_ID": "DOC1",
                "DOCUMENT_RECORD_INDEX": 2,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": "ENTTY1",
            },
        ],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {"DOC1": {"out_of_range": [2]}},
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
    "large_number_of_duplicates": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": i, "DOCUMENT_RECORD_COUNT": 1000}
            for i in range(1, 1001)
        ]
        + [
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": i, "DOCUMENT_RECORD_COUNT": 1000}
            for i in range(1, 1001)
        ],
        "expected_results": {
            "missing": {},
            "identical_duplicates": {"DOC1": {i: 1 for i in range(1, 1001)}},
            "different_duplicates": {},
            "indexing_errors": {},
            "invalid_document_counts": {},
            "distinct_stories_count": 1,
        },
    },
}

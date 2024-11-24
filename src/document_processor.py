"""
This module provides the DataProcessor class for processing and analyzing document records.

The DataProcessor class includes methods for validating document IDs, counting distinct stories,
checking for missing or invalid document record indices, handling duplicate entries, and identifying
and logging any records with inconsistent counts or invalid indices.

Attributes:
    records (list): List of JSON records.
    document_records (dict): Dictionary to store document records.
    results (dict): Dictionary to store the results of the analysis.
"""


class DataProcessor:
    """
    A class to process and analyze document records.

    Attributes:
        records (list): List of JSON records to be processed.
        document_records (dict): Dictionary to store document records, including indices and counts.
        results (dict): Dictionary to store the results of the analysis, including missing indices, duplicates, and errors.
    """

    def __init__(self, records):
        """
        Initializes the DataProcessor class with the provided records.

        Args:
            records (list): List of JSON records to be processed.

        Attributes:
            records (list): List of JSON records to be processed.
            document_records (dict): Dictionary to store document records, including indices and counts.
            results (dict): Dictionary to store the results of the analysis, including missing indices, duplicates, and errors.
        """
        self.records = records
        self.document_records = {}
        self.results = {
            "missing": {},
            "identical_duplicates": {},
            "different_duplicates": {},
            "indexing_errors": {},
            "invalid_document_counts": {},
            "distinct_stories_count": 0,
        }

    def process_analytics(self):
        """
        Processes the JSON records to find and log missing indices, duplicate records, and indexing errors.

        This method performs a full analysis of the document records by:
        - Validating document IDs to ensure they are non-empty strings.
        - Counting distinct stories based on valid 'RP_DOCUMENT_ID' values.
        - Checking for missing or invalid document record indices.
        - Handling duplicate entries, both identical and different.
        - Identifying and logging any records with inconsistent counts or invalid indices.

        Returns:
            dict: A dictionary containing the analysis results, including:
                - 'missing': Records missing indices for a document.
                - 'identical_duplicates': Records where identical duplicates were found.
                - 'different_duplicates': Records with differing duplicates.
                - 'indexing_errors': Errors related to indexing, such as out-of-range or invalid types.
                - 'invalid_document_counts': Records with invalid document counts.
                - 'distinct_stories_count': The number of unique document stories.

        Side Effects:
            - Modifies `self.results` with analysis outcomes.
            - Modifies `self.document_records` to keep track of document counts, indices, and duplicates.
        """

        self.identify_invalid_document_ids()

        # Count distinct stories after ensuring all document IDs are valid strings

        self.count_distinct_stories()

        for record in self.records:
            document_id = self.get_field(record, "RP_DOCUMENT_ID")

            # Initialize document record if valid and not already present.
            # If the document ID is valid and not already initialized, the document record will be created.
            # If the document ID is invalid or already exists, it will be skipped.
            # The existing document record will remain untouched if it was already initialized.

            if not self.initialize_document_record(document_id):
                # Skip this record if document ID is invalid or already exists.
                # (should've been controlled already)
                continue

            # Get DOCUMENT_RECORD_INDEX and DOCUMENT_RECORD_COUNT
            # Use the getter methods to fetch the indices and counts
            record_index = self.get_field(record, "DOCUMENT_RECORD_INDEX")
            record_count = self.get_field(record, "DOCUMENT_RECORD_COUNT")

            self.check_and_log_document_count(record_count, document_id)
            self.handle_document_count(record_count, document_id)

            # Validate DOCUMENT_RECORD_INDEX
            if not self.validate_index(record_index, document_id):
                continue  # Skip if the index is invalid.

            # Handle duplicate indices
            self.handle_duplicates(record, record_index, document_id)

        # Now call the `identify_missing_indices` method to log missing, extra
        # indices, and duplicates
        self.identify_missing_indices()

        return self.results

    def count_distinct_stories(self):
        """
        Counts and logs the number of distinct document stories based on their 'RP_DOCUMENT_ID'.

        This method iterates through the records and identifies unique document IDs.
        A distinct document is defined by the presence of a unique 'RP_DOCUMENT_ID' field.

        Returns:
            int: The number of distinct stories (unique document IDs).

        Side Effect:
            - Updates `self.results['distinct_stories_count']` with the count of distinct stories.
        """

        distinct_document_ids = {
            record["RP_DOCUMENT_ID"]
            for record in self.records
            if "RP_DOCUMENT_ID" in record
            and isinstance(record["RP_DOCUMENT_ID"], str)
            and record["RP_DOCUMENT_ID"].strip()
        }

        self.results["distinct_stories_count"] = len(distinct_document_ids)
        return self.results["distinct_stories_count"]

    def identify_invalid_document_ids(self):
        """
        Identifies and logs invalid document IDs (non-strings or empty) for each record.

        This method checks if the 'RP_DOCUMENT_ID' is a non-empty string, and if not, logs the error with
        the document's 'RP_ENTITY_ID' and the entire record.

        Side Effects:
            - Logs invalid document IDs to `self.results['indexing_errors']['invalid_document_ids']`.
        """
        # Set to keep track of invalid document IDs to avoid duplicate logging
        logged_invalid_document_ids = set()

        for record in self.records:
            document_id = record.get("RP_DOCUMENT_ID")

            # Check if the document ID is not a non-empty string (i.e., None or
            # empty string)
            if not document_id or not isinstance(document_id, str) or not document_id.strip():
                # Log invalid document IDs along with their RP_ENTITY_ID
                rp_entity_id = self.get_field(record, "RP_ENTITY_ID")

                # Ensure this record is only logged once
                if document_id not in logged_invalid_document_ids:
                    self.results["indexing_errors"].setdefault("invalid_document_ids", []).append(
                        {
                            "RP_DOCUMENT_ID": document_id,
                            "RP_ENTITY_ID": rp_entity_id,
                            "record": record,
                        }
                    )
                    logged_invalid_document_ids.add(document_id)

    def initialize_document_record(self, document_id):
        """
        Checks if the document ID is valid and not already initialized in document_records.
        Initializes the document record if valid.

        Args:
            document_id (str): The document ID to check and initialize.

        Returns:
            bool: True if the document ID is valid and was initialized, False if the document ID is invalid.
        """
        # Skip invalid document IDs (non-strings or empty strings)
        if not isinstance(document_id, str) or not document_id.strip():
            return False  # Invalid document ID, do not initialize.

        # Initialize the document record if it's not already present.
        # If the document ID already exists, it will not be modified.
        if document_id not in self.document_records:
            self.document_records[document_id] = {
                "indices": set(),
                "expected_count": None,
                "data": {},
                "identical_duplicates": {},
                "different_duplicates": {},
                "logged_out_of_range": set(),
            }

        return True  # Document record was initialized or already exists.

    def check_and_log_document_count(self, record_count, document_id):
        """
        Validates and logs issues related to the document's record count.

        Args:
            record_count (int/str): The provided count of records for the document.
            document_id (str): The ID of the document being validated.

        This method ensures that the record count is a valid positive integer and not zero.
        If the count is invalid (e.g., contains decimals, non-numeric characters, or is zero),
        it is logged under `self.results['invalid_document_counts']`.

        Side Effects:
            - Logs invalid document counts to `self.results['invalid_document_counts']` under the document's ID.
        """

        # Check if record_count is an integer and valid (positive, non-zero)
        if isinstance(record_count, int) and not isinstance(record_count, bool):
            if record_count <= 0:  # Check if it's zero or negative
                self.results["invalid_document_counts"].setdefault(document_id, []).append(
                    record_count
                )
            # Exit after logging if it's a valid integer or an invalid
            # (non-positive) integer
            return

        # Check if record_count is a string representation of an integer
        if isinstance(record_count, str) and record_count.isdigit():
            converted_count = int(record_count)
            if converted_count <= 0:  # Check if converted record count is non-positive
                self.results["invalid_document_counts"].setdefault(document_id, []).append(
                    record_count
                )  # Log the original string
            return

        # Log non-numeric values (string or other type) as invalid
        self.results["invalid_document_counts"].setdefault(document_id, []).append(record_count)

    def handle_document_count(self, record_count, document_id):
        """
        Ensures consistency between the provided record count and the expected count for a document.

        Args:
            record_count (int): The number of records provided for the document. This corresponds
                to the total number of parts/segments that make up the document.
            document_id (str): The unique identifier of the document being processed.

        This method performs the following actions:
        - If the `expected_count` for the document has not been set, it initializes it using the `record_count`.
        - If the `expected_count` is already set but does not match the `record_count`, it logs a 'count_mismatch' error in
        the `results['indexing_errors']` under the document ID.

        This method is typically called when processing records to ensure that the expected number of document segments
        is consistent with the actual number provided. Inconsistent counts might indicate errors in data integrity.

        Side Effect:
        - Updates the `self.document_records[document_id]['expected_count']` field.
        - Logs count mismatches to `self.results['indexing_errors']`.
        """

        if (
            isinstance(record_count, int)
            and not isinstance(record_count, bool)
            and record_count > 0
        ):
            expected_count = self.document_records[document_id]["expected_count"]
            if expected_count is None:
                self.document_records[document_id]["expected_count"] = record_count
            elif expected_count != record_count:
                self.results["indexing_errors"].setdefault(document_id, {}).setdefault(
                    "count_mismatch", []
                ).append(record_count)

    def validate_index(self, record_index, document_id):
        """
        Validates the 'DOCUMENT_RECORD_INDEX' for the provided document.

        Args:
            record_index (int/str): The index of the current record. Should be an integer.
            document_id (str): The ID of the document being validated.

        This method performs the following validations:
        - Attempts to convert `record_index` to an integer if it's not already one. Logs an error if conversion fails.
        - Ensures that the index falls within the valid range (1 to `expected_count`). Logs out-of-range indices to `self.results['indexing_errors']`.
        - If the index is invalid or out of range, the method returns False to indicate the record should be skipped.

        Returns:
            bool: True if the index is valid and within range, False otherwise.

        Side Effects:
            - Logs invalid indices and out-of-range errors to `self.results['indexing_errors']`.
        """

        if isinstance(record_index, bool) or not isinstance(record_index, int):
            try:
                if isinstance(record_index, bool):
                    self.results["indexing_errors"].setdefault(document_id, {}).setdefault(
                        "invalid_type", []
                    ).append(
                        f"Expected: int, Found: {type(record_index).__name__} for index: {record_index}"
                    )
                    return False
                record_index = int(record_index)
            except (ValueError, TypeError):
                self.results["indexing_errors"].setdefault(document_id, {}).setdefault(
                    "invalid_type", []
                ).append(
                    f"Expected: int, Found: {type(record_index).__name__} for index: {record_index}"
                )
                return False

        # Ensure the index is within range
        expected_count = self.document_records[document_id]["expected_count"]
        if expected_count and (record_index < 1 or record_index > expected_count):
            if record_index not in self.document_records[document_id]["logged_out_of_range"]:
                self.results["indexing_errors"].setdefault(document_id, {}).setdefault(
                    "out_of_range", []
                ).append(record_index)
                self.document_records[document_id]["logged_out_of_range"].add(record_index)
            return False  # Skip this record as its index is out of bounds
        return True

    def handle_duplicates(self, record, record_index, document_id):
        """
        Identifies and logs duplicate records for a given document.

        Args:
            record (dict): The current record being processed.
            record_index (int): The index of the current record.
            document_id (str): The ID of the document being processed.

        This method checks if the `record_index` already exists for the given document. If it does:
        - If the existing data matches the current record, it increments the identical duplicate count.
        - If the existing data differs, it increments the different duplicate count.

        If the `record_index` is not present, the method stores the current record in `self.document_records`.

        Side Effects:
            - Updates `self.document_records` to track duplicate counts and store new records.
            - Logs identical and different duplicates.
        """
        # Retrieve the data for the given document ID
        doc_data = self.document_records[document_id]

        # Check if the current record index already exists in the document's data
        if record_index in doc_data["data"]:
            # If the record index exists, fetch the existing record
            existing_data = doc_data["data"][record_index]

            # If the existing record is identical to the current one, increment
            # the identical duplicates count
            if existing_data == record:
                # Update or initialize the identical duplicate count for the current record index
                doc_data["identical_duplicates"][record_index] = (
                    doc_data["identical_duplicates"].get(record_index, 0) + 1
                )
                # Log identical duplicates directly here
                self.results.setdefault("identical_duplicates", {}).setdefault(document_id, {})[
                    record_index
                ] = doc_data["identical_duplicates"][record_index]
            else:
                # If the existing record differs from the current one, increment the different duplicates count
                doc_data["different_duplicates"][record_index] = (
                    doc_data["different_duplicates"].get(record_index, 0) + 1
                )
                # Log different duplicates directly here
                self.results.setdefault("different_duplicates", {}).setdefault(document_id, {})[
                    record_index
                ] = doc_data["different_duplicates"][record_index]

        # If the record index doesn't exist in the document's data, store the current record
        else:
            # Add the new record to the data dictionary under the record index
            doc_data["data"][record_index] = record

            # Add the record index to the set of indices for the document
            doc_data["indices"].add(record_index)

    def identify_missing_indices(self):
        """
        Identifies and logs missing record indices for each document.

        This method checks the expected number of records for each document (`expected_count`)
        and compares it to the indices that are present. Any missing indices (i.e., record indices
        that should exist but don't) are logged under `self.results['missing']`.

        Additionally, the method logs any identified duplicates and unexpected indices.

        Side Effects:
            - Logs missing indices to `self.results['missing']`.
            - Logs duplicate records to `self.results['identical_duplicates']` and `self.results['different_duplicates']`.
            - Logs unexpected indices to `self.results['extra_indices']` if `valid_indices` exceeds `expected_count`.
        """

        for document_id, doc_data in self.document_records.items():
            expected_count = doc_data["expected_count"]
            if expected_count is not None:
                # Filter out invalid indices before calculating missing indices
                valid_indices = {
                    index
                    for index in doc_data["indices"]
                    if isinstance(index, int) and not isinstance(index, bool)
                }

                # Identify indices outside the expected range (extra indices)
                extra_indices = {index for index in valid_indices if index > expected_count}
                if extra_indices:
                    # Log the extra indices, which are larger than the expected count
                    self.results.setdefault("extra_indices", {}).setdefault(document_id, []).extend(
                        extra_indices
                    )

                # Calculate missing indices (indices expected but not present)
                missing_indices = set(range(1, expected_count + 1)) - valid_indices
                if missing_indices:
                    self.results.setdefault("missing", {})[document_id] = list(
                        sorted(missing_indices)
                    )

    def get_field(self, record, field_name):
        """
        Retrieves a field from the record.

        Args:
            record (dict): The record from which to fetch the field.
            field_name (str): The field name to retrieve.
            default: The default value to return if the field is missing.

        Returns:
            The field value if it exists, or the default value.
        """
        return record.get(field_name)

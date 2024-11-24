"""
This module provides validation functions for JSON records.

The functions in this module validate various fields in the records, such as
RP_DOCUMENT_ID and RP_ENTITY_ID, and check for missing or invalid values.
"""

import re


def validate_rp_document_id(record):
    """
    Validates the RP_ENTITY_ID format for each record in the JSON file.

    Args:
        records (list): List of JSON records to be validated.

    Returns:
        list: A list of tuples containing invalid RP_ENTITY_IDs and their corresponding document IDs and indices.
    """
    rp_document_id = record.get("RP_DOCUMENT_ID")
    document_index = record.get("DOCUMENT_RECORD_INDEX")

    if rp_document_id in [None, ""] or (
        isinstance(rp_document_id, str) and rp_document_id.strip() == ""
    ):
        # Return a tuple with the error information (None or empty document ID)
        return ("", None, document_index) if rp_document_id == "" else (None, None, document_index)

    if isinstance(rp_document_id, bool):
        return (None, None, document_index)

    return None


def check_missing_rp_entity_id(record):
    """
    Checks if the RP_ENTITY_ID is missing or None.

    Args:
        record (dict): A single JSON record.

    Returns:
        tuple or None: A tuple containing the error information or None if present.
    """
    rp_entity_id = record.get("RP_ENTITY_ID")
    rp_document_id = record.get("RP_DOCUMENT_ID")
    document_index = record.get("DOCUMENT_RECORD_INDEX")

    if "RP_ENTITY_ID" not in record or rp_entity_id is None:
        return (None, rp_document_id, document_index)

    return None


def validate_rp_entity_id_format(rp_entity_id, rp_document_id, document_index):
    """
    Validates the format of RP_ENTITY_ID.

    Args:
        rp_entity_id (str): The RP_ENTITY_ID to validate.
        rp_document_id (str): The corresponding document ID.
        document_index (int): The index of the document in the record list.

    Returns:
        tuple or None: A tuple containing the error information or None if valid.
    """
    pattern = r"^[A-Z0-9]{6}$"  # 6 uppercase letters or digits
    rp_entity_id_str = str(rp_entity_id).strip()

    if not re.match(pattern, rp_entity_id_str):
        return (rp_entity_id_str, rp_document_id, document_index)

    return None


def validate_rp_entity_ids(records):
    """
    Validates the RP_ENTITY_ID format for each record in the JSON file.

    Args:
        records (list): List of JSON records.

    Returns:
        list: A list of tuples containing invalid RP_ENTITY_IDs and their corresponding document IDs and indices.
    """
    errors = []

    for record in records:
        rp_document_id = record.get("RP_DOCUMENT_ID")
        rp_entity_id = record.get("RP_ENTITY_ID")
        document_index = record.get("DOCUMENT_RECORD_INDEX")

        # First we validate the RP_DOCUMENT_ID, then check if RP_ENTITY_ID is missing or empty
        # Then we validate the format of RP_ENTITY_ID
        # If any of the checks fail, we add the error to the list and continue to the next record

        doc_error = validate_rp_document_id(record)
        if doc_error:
            errors.append(doc_error)
            continue

        missing_rp_error = check_missing_rp_entity_id(record)
        if missing_rp_error:
            errors.append(missing_rp_error)
            continue

        format_error = validate_rp_entity_id_format(rp_entity_id, rp_document_id, document_index)
        if format_error:
            errors.append(format_error)

    return errors

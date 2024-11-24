"""
This module contains functions for performing teardown operations, such as cleaning up temporary directories.
It is intended to be used at the end of a process to ensure that any temporary directories created during the
process are properly cleaned up.

Functions:
    perform_teardown(config): Perform teardown operations based on the provided configuration.
"""

from .data_loader import cleanup_temp_directory


# Right now we only have this as teardown function, but this is where
# other teardown operations can be added in the future.


def teardown(config):
    """
    Perform teardown operations such as cleaning up temporary directories.

    This function is intended to be called at the end of a process to ensure that any temporary
    directories created during the process are properly cleaned up. It takes a configuration
    dictionary `config` which specifies various options for the teardown process.

    Args:
        config (dict): A dictionary containing configuration options for the teardown process.
            - temp_dir (str, optional): The path to the temporary directory to be cleaned up.

    Example:
        perform_teardown({
            "temp_dir": "/path/to/temp/dir"
        })
    """
    temp_dir = config.get("temp_dir")

    if temp_dir:
        cleanup_temp_directory(temp_dir)

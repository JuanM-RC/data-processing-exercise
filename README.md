# Document Analytics and Validation

This project processes and validatesa lists of JSON records (compressed in .rar or not) to identify and log missing indices, duplicate records, and indexing errors. It also validates `RP_ENTITY_ID` formats. After this, it logs the results on console
and a log file.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Logging](#logging)
- [Testing](#testing)

## Features

- **Document Analytics**: Processes JSON records to find and log missing indices, duplicate records, and indexing errors.
- **RP_ENTITY_ID Validation**: Validates the format of `RP_ENTITY_ID` and indexes any errors.
- **Logging**: Logs the results of the analytics and validation processes to both the console and a log file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/juanM-RC/data-processing-exercise.git
    cd document-analytics
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1.  Run the following command:

    ```sh
    export PYTHONPATH=$PYTHONPATH:/path/to/your/directory   
    ```

2.  Run the main script with the file path argument:
    When running the script, provide the path to the file as an argument for main(). For example:

    ```sh
    python3 src/main.py fixtures/rt-feed-record.rar
    ```

2. The results will be logged to both the console and a log file in the `logs` directory.

## Docker Usage
You can also run the application inside a Docker container. This allows you to run the application without worrying about dependencies or environment setup.

### Prerequisites

    - Install Docker
    - Ensure the Docker daemon is running
### Steps to Run via Docker

1. Build the Docker image: Inside the project directory, run:

    ```sh
    docker build -t my-python-container .
    ```

2. Run the Docker container: To process files and output logs to a specific directory on your host system, use the docker run command with volume mappings. Here's an example of how to run the container:

    ```sh
    docker run --rm \
    -v /path/to/your/input:/data \
    -v /path/to/your/logs:/logs \
    my-python-container \
    python3 src/main.py /data/your-input-file /logs
    ```

-v /path/to/your/input:/usr/src/app/data: Mounts the input file directory from your local machine to the container.
-v /path/to/your/logs:/usr/src/app/logs: Mounts the output directory for logs from your local machine to the container.
Replace /path/to/your/input with the path to the directory containing your input file, and /path/to/your/logs with the path to your log directory.


## Project Structure

    document-analytics/
    ├── src/
    │   ├── document_processor.py  # Contains the DataProcessor class and its methods
    │   ├── utils/
    │   │   ├── logging.py  # Contains logging setup and formatting functions
    │   │   └── validation.py  # Contains functions to validate RP_ENTITY_ID
    │   └── helpers/
    │       └── data_loader.py  # Contains functions to load and clean up JSON data
    ├── fixtures/  # Directory to place files containing JSON data for processing
    ├── logs/  # Directory where log files will be stored
    ├── tests/  # Directory containing tests
    │   └── sample_data/  # Directory containing sample data for tests
    ├── requirements.txt  # List of required dependencies
    └── README.md  # Project documentation




## Logging

The logging configuration is set up to log messages to both the console and a log file. The log file is stored in the `logs` directory, with a filename based on the processed file name.

### Example Log Output

    2024-11-21 22:48:10,234 -  open_json

    Number of distinct stories: 273

    Document ID 0B31D33076B73E35F140F4701F69168C:
        - Missing indices: [1, 2, 3, 4, 24]
        - Identical duplicate indices: index: 11, repeated: 5 times
        - Different duplicate indices: index: 11, repeated: 1 time
        - Invalid Type Errors:
            Expected: int, Found: str for index: kjasd
            Expected: int, Found: str for index: string
        - Out of Range Errors:
            Out of range index: -2
            Out of range index: 0
            Out of range index: 333

    Document ID E4086102EB4BAFB97DF4765B69B1DB9A:
        - Missing indices: [19, 27]
        - Out of Range Errors:
            Out of range index: 28
            Out of range index: 12229

    Document ID CECFA0D206F9A331099A7C65765A3FBD:
        - Missing indices: [2]

    --- RP Entity ID Validation Logs ---

    Document ID E4086102EB4BAFB97DF4765B69B1DB9A:
        - Invalid RP_ENTITY_ID: 'EA73sss5B' at index 22

    Document ID D7D1B9C1E0B83CA2AFC31261E8FBBDC1:
        - Invalid RP_ENTITY_ID: 'F3548sda4' at index 7
        - Invalid RP_ENTITY_ID: '8C23A' at index 17

    Document ID CECFA0D206F9A331099A7C65765A3FBD:
        - Invalid RP_ENTITY_ID: '' at index 1
        - Invalid RP_ENTITY_ID: '' at index 3

## Testing

To run the tests, use the following command:

```sh
pytest
```





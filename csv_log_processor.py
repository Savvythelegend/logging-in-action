import logging
import pandas as pd
import time
import numpy as np
from pathlib import Path
from typing import Union

# Configure logging
LOG_FILE = "data_processing.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_dummy_csv(file_path: Union[str, Path]) -> None:
    """
    Creates a dummy CSV file with sample data, including some missing values.

    Args:
        file_path (str | Path): Path where the CSV file will be saved.
    """
    data = {
        "ID": np.arange(1, 11),
        "Name": [f"User_{i}" for i in range(1, 11)],
        "Age": np.random.randint(18, 60, size=10),
        "Salary": np.random.randint(30000, 100000, size=10),
        "Department": [np.random.choice(["HR", "IT", "Finance", None]) for _ in range(10)]
    }

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    logging.info("Dummy CSV file '%s' created successfully.", file_path)

def process_csv(file_path: Union[str, Path]) -> None:
    """
    Processes the given CSV file:
    - Loads the CSV
    - Logs any missing values
    - Replaces missing values with 'UNKNOWN'
    - Logs the time taken for processing

    Args:
        file_path (str | Path): Path to the CSV file to process.
    """
    try:
        logging.info("Starting processing for file: %s", file_path)
        start_time = time.time()

        # Load CSV into DataFrame
        df = pd.read_csv(file_path)

        # Count total missing values
        total_missing = df.isnull().sum().sum()

        if total_missing > 0:
            logging.warning("File '%s' contains %d missing values", file_path, total_missing)

        # Fill missing values
        df.fillna("UNKNOWN", inplace=True)

        elapsed = time.time() - start_time
        logging.info("Processing completed in %.2f seconds", elapsed)

    except Exception as e:
        logging.exception("Failed to process file '%s': %s", file_path, str(e))

def main():
    """
    Main execution function:
    - Creates a dummy CSV
    - Processes the CSV
    """
    csv_file = Path("data.csv")
    create_dummy_csv(csv_file)
    process_csv(csv_file)

if __name__ == "__main__":
    main()

import logging
import pandas as pd
import time
import numpy as np

# Configure logging
logging.basicConfig(filename="data_processing.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Create a dummy CSV file
def create_dummy_csv(file_path):
    data = {
        "ID": np.arange(1, 11),
        "Name": [f"User_{i}" for i in range(1, 11)],
        "Age": np.random.randint(18, 60, size=10),
        "Salary": np.random.randint(30000, 100000, size=10),
        "Department": [np.random.choice(["HR", "IT", "Finance", None]) for _ in range(10)]  # Some missing values
    }
    
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    logging.info(f"Dummy CSV file '{file_path}' created successfully.")

# Function to process the CSV file
def process_csv(file_path):
    try:
        logging.info(f"Starting processing for {file_path}")
        start_time = time.time()

        # Load CSV
        df = pd.read_csv(file_path)

        # Check for missing values
        missing_values = df.isnull().sum().sum() 
        """
        A    1
        B    1
        C    1
        dtype: int64
        This gives the count of missing values per column.

        3️ df.isnull().sum().sum() → Total Missing Values
        The second .sum() adds up the values from all columns:

        1 (A) + 1 (B) + 1 (C) = 3
        """

        if missing_values > 0:
            logging.warning(f"File {file_path} contains {missing_values} missing values")

        # Process data (Dummy operation)
        df.fillna("UNKNOWN", inplace=True)
        """
        Breaking it Down
        df.fillna("UNKNOWN")

        Replaces all NaN (missing values) in the DataFrame with "UNKNOWN".
        Returns a new DataFrame (does not modify df in place unless specified).
        inplace=True

        Updates df directly instead of returning a new DataFrame.
        Without inplace=True, you'd need to reassign it:
        df = df.fillna("UNKNOWN")
        """

        end_time = time.time()
        logging.info(f"Processing completed in {end_time - start_time:.2f} seconds")

    except Exception as e:
        logging.error(f"Error processing {file_path}: {str(e)}")

# Run the process
csv_file = "data.csv"
create_dummy_csv(csv_file)  # Generate dummy CSV
process_csv(csv_file)  # Process the CSV

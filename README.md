# **Logging — Structured Notes**

We’ll follow an **intuitive learning approach**:

### Learning Path:

* **Step 1:** What is logging & why use it? (Quick theory)
* **Step 2:** Basic logging (Hands-on coding)
* **Step 3:** Advanced logging (Different log levels, handlers, and formatting)
* **Step 4:** Real-world use cases (ML pipeline logging, Flask API logs, file logging)
* **Step 5:** Build a **mini-project** where logging is essential

---

## **Step 1: What is Logging & Why Use It?**

### What is Logging?

Logging is a way to **track events in a program** during its execution. It is a better alternative to `print()` for the following reasons:

* Helps in debugging without cluttering the console
* Tracks errors in production environments
* Saves logs to a file for audit or future reference
* Monitors machine learning model training, performance metrics, and data-related issues

### Why Not Use `print()`?

* `print()` is temporary and does not store logs
* Lacks control over log levels (info, warning, error)
* Difficult to filter logs in large applications
* `logging` is structured, supports filtering, and is file-writable

---

## **Step 2: Hands-on — Basic Logging**

### Example:

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")
```

### Output:

```
WARNING:root:This is a WARNING message  
ERROR:root:This is an ERROR message  
CRITICAL:root:This is a CRITICAL message
```

### Note:

By default, only messages with level WARNING and above are shown. To see DEBUG and INFO, `level=logging.DEBUG` must be set.

---

## **Step 3: Writing Logs to a File**

### Example:

```python
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("This will be logged into app.log")
```

### Output in `app.log`:

```
2025-03-13 12:45:00 - INFO - This will be logged into app.log
```

---

## **Step 4: Real-World Use Cases**

### 1. Logging in a Machine Learning Pipeline

```python
import logging
import time

logging.basicConfig(
    filename="ml_training.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting model training...")

for epoch in range(1, 6):
    accuracy = 0.80 + (epoch * 0.02)
    loss = 0.5 - (epoch * 0.05)
    logging.info(f"Epoch {epoch}: Accuracy = {accuracy}, Loss = {loss}")
    time.sleep(1)

logging.info("Model training completed!")
```

**Use Case:** Helps monitor training and diagnose failures or performance issues.

---

### 2. Logging in a Flask API

```python
from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():
    logging.info("Home page accessed")
    return "Welcome to the Flask API!"

@app.route("/error")
def error():
    logging.error("Error endpoint triggered!")
    return "This is an error!", 500

if __name__ == "__main__":
    app.run(debug=True)
```

**Use Case:** Log incoming requests and errors for debugging purposes.

---

## **Step 5: Mini Project — Logging in a Data Processing Pipeline**

### Objective:

Create a script to process CSV files and log:

* Errors
* Progress
* Time taken

### Code:

```python
import logging
import pandas as pd
import time

logging.basicConfig(
    filename="data_processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_csv(file_path):
    try:
        logging.info(f"Starting processing for {file_path}")
        start_time = time.time()

        df = pd.read_csv(file_path)

        missing_values = df.isnull().sum().sum()
        if missing_values > 0:
            logging.warning(f"File {file_path} contains {missing_values} missing values")

        df.fillna("UNKNOWN", inplace=True)

        end_time = time.time()
        logging.info(f"Processing completed in {end_time - start_time:.2f} seconds")

    except Exception as e:
        logging.error(f"Error processing {file_path}: {str(e)}")

process_csv("data.csv")
```

### How to Test:

1. Create a CSV file with missing values
2. Run the script
3. Check `data_processing.log` for output

---

## **Advanced Logging Concepts**

---

### Handlers — What Are They?

#### Why Use Handlers?

You may want:

* Logs to appear in both console and file
* Log files to stay under a certain size

#### Example:

```python
import logging

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("mylog.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("This will be saved in a file AND shown in terminal")
logger.warning("Warning message here!")
```

**Console Output:**

```
INFO: This will be saved in a file AND shown in terminal  
WARNING: Warning message here!
```

**File Output (`mylog.log`) includes timestamped entries.**

---

### Rotating Logs

#### Why Rotate Logs?

If a log file grows too large (e.g., 1GB), it can consume disk space. **Rotating logs** prevents this by capping file size and managing old files.

#### Example:

```python
from logging.handlers import RotatingFileHandler
import logging

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler("mylog.log", maxBytes=5000, backupCount=3)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(file_handler)

for i in range(1000):
    logger.info(f"This is log message {i}")
```

#### What Happens:

* When `mylog.log` exceeds 5000 bytes, it becomes `mylog.log.1`
* A new `mylog.log` is created
* Keeps only 3 backups: `.1`, `.2`, `.3`
* Older logs are deleted automatically

---

### `backupCount` and `maxBytes` Explained

* `maxBytes=5000`: When current log hits 5000 bytes, rotation occurs
* `backupCount=3`: Retains up to 3 previous log files
* Older backups beyond `.3` are deleted

---

### Checking Log File Sizes

```python
import os

log_files = ["mylog.log", "mylog.log.1", "mylog.log.2", "mylog.log.3"]

for log in log_files:
    if os.path.exists(log):
        print(f"{log}: {os.path.getsize(log)} bytes")
```

---

## **Recap**

* **Basic Logging**: Levels like DEBUG, INFO, WARNING, etc.
* **File Logging**: Save logs using `basicConfig()`
* **Real-World Use**: ML pipelines, APIs, data workflows
* **Handlers**: Combine multiple outputs (file, console)
* **RotatingFileHandler**: Manage log file size and retention

---
